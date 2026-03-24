from django.contrib import admin
from .models import EmailHistory


@admin.register(EmailHistory)
class EmailHistoryAdmin(admin.ModelAdmin):
    # Colunas exibidas na lista principal
    list_display = ('user', 'subject', 'category', 'file_name', 'created_at')

    # Filtros laterais
    list_filter = ('category', 'created_at', 'user')

    # Busca por assunto, nome do usuário ou categoria
    search_fields = ('subject', 'user__username', 'category', 'file_name')

    # Ordenação
    ordering = ('-created_at',)

    # CAMPOS APENAS LEITURA
    readonly_fields = (
        'user', 'subject', 'body', 'file_name',
        'file_content', 'category', 'ai_response', 'created_at'
    )

    # Organização visual dos campos no detalhe do registro
    fieldsets = (
        ('Informações do Usuário', {
            'fields': ('user', 'created_at')
        }),
        ('Conteúdo do Email', {
            'fields': ('subject', 'body')
        }),
        ('Arquivo Relacionado', {
            'fields': ('file_name', 'file_content'),
            'classes': ('collapse',),
        }),
        ('Análise da IA', {
            'fields': ('category', 'ai_response'),
        }),
    )

    # def has_add_permission(self, request):
    #     return False
