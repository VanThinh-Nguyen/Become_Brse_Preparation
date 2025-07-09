# chat/views.py
import time
import json
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def sse_view(request):
    def event_stream():
        lines = [
            "**Xin chào!** Tôi là một *AI chatbot*.\n\n",
            "Dưới đây là bảng thông tin:\n\n",
            "| Tên | Vai trò |\n",
            "|-----|----------|\n",
            "| Thịnh | Người dùng |\n",
            "| Bot   | Trợ lý  |\n\n",
            "Cảm ơn bạn đã sử dụng dịch vụ! 🎉"
        ]

        for i, line in enumerate(lines):
            message = {
                "session_id": "id_001",
                "data": {
                    "type": "markdown",
                    "value": line
                }
            }
            yield f"event: message\nid: {i}\ndata: {json.dumps(message)}\n\n"
            time.sleep(0.5)  # giả lập typing delay

    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        return JsonResponse({"status": "success", "message": "Message sent!"})