from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.emails.serializers import EmailRequestSerializer
from services.ai_orchestrator import process_email
from services.file_utils import extract_text_from_file
from .models import EmailHistory


@login_required(login_url='/login/')
def home(request):
    result = None

    if request.method == "POST":
        data = request.POST.copy()

        # Se houver arquivo, adiciona no dict
        if 'file' in request.FILES:
            data['file'] = request.FILES['file']

        serializer = EmailRequestSerializer(data=data)
        if serializer.is_valid():
            # Construir texto completo do email: subject + body + conteúdo do arquivo (se houver)
            email_parts = []

            subject = serializer.validated_data.get("subject", "").strip()
            body = serializer.validated_data.get("body", "").strip()
            file = serializer.validated_data.get("file")

            if subject:
                email_parts.append(f"Subject: {subject}")
            if body:
                email_parts.append(f"Body:\n{body}")
            if file:
                try:
                    file_text = extract_text_from_file(file)
                    if file_text:
                        email_parts.append(f"File Content:\n{file_text}")
                except Exception as e:
                    email_parts.append(
                        f"File Content: [Erro ao ler arquivo: {str(e)}]")

            full_text = "\n\n".join(email_parts)

            # Chama o orquestrador
            result = process_email(full_text)

            if result.get("category") != "ERROR":
                # SALVAR NO HISTÓRICO
                EmailHistory.objects.create(
                    user=request.user,
                    subject=subject,
                    body=body,
                    file_name=file.name if file else None,
                    file_content=file_text if file else None,
                    category=result["category"],
                    ai_response=result["response"]
                )

        else:
            result = {
                "category": "ERRO",
                "response": serializer.errors
            }
    else:
        serializer = EmailRequestSerializer()

    # Lista de campos para render no template
    fields = []
    for name, field in serializer.fields.items():
        fields.append({
            "name": name,
            "type": field.__class__.__name__,
            "required": field.required
        })

    history = EmailHistory.objects.filter(user=request.user)[:10]

    return render(request, "emails/home.html", {"fields": fields, "result": result, "history": history})
