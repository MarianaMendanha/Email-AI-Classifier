from rest_framework import serializers


class EmailCategoryChoices:
    PRODUTIVO = "PRODUTIVO"
    IMPRODUTIVO = "IMPRODUTIVO"

    CHOICES = [
        (PRODUTIVO, "Produtivo"),
        (IMPRODUTIVO, "Improdutivo"),
    ]


class EmailRequestSerializer(serializers.Serializer):
    subject = serializers.CharField(
        max_length=255, required=False, allow_blank=True)
    body = serializers.CharField(required=False, allow_blank=True)
    file = serializers.FileField(required=False)

    def validate(self, data):
        if not data.get("file") and not (data.get("subject") or data.get("body")):
            raise serializers.ValidationError(
                "Provide either a file or subject/body."
            )
        return data

    def get_full_text(self):
        subject = self.validated_data.get("subject", "")
        body = self.validated_data.get("body", "")
        file = self.validated_data.get("file")

        file_content = ""

        if file:
            file_content = file.read().decode("utf-8", errors="ignore")

        return f"""
        Subject: {subject}

        Body:
        {body}

        File Content:
        {file_content}
        """


class EmailResponseSerializer(serializers.Serializer):
    category = serializers.ChoiceField(choices=EmailCategoryChoices.CHOICES)
    response = serializers.CharField()

    def validate_response(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Response cannot be empty")
        return value
