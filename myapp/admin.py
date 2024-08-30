from django.contrib import admin
from django.core.mail import send_mail
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'comment', 'reply')
    actions = ['send_reply']

    def send_reply(self, request, queryset):
        for comment in queryset:
            if comment.reply:
                try:
                    send_mail(
                        subject='Reply to Your Comment',
                        message=f'Dear {comment.name},\n\n{comment.reply}\n\nBest regards,\nAdmin Team',
                        from_email='rwothongeojulius052@gmail.com',
                        recipient_list=[comment.email],
                        fail_silently=False,
                    )
                    self.message_user(request, f"Reply sent to {comment.email}")
                except Exception as e:
                    self.message_user(request, f"Failed to send email to {comment.email}. Error: {e}", level='error')
            else:
                self.message_user(request, f"No reply found for {comment.name}", level='error')

    send_reply.short_description = 'Send reply to selected comments'

admin.site.register(Comment, CommentAdmin)
