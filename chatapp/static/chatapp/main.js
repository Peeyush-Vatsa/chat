const message_field = document.getElementById('message');

let chatSocket = null;

const connectSocket = () => {
    chatSocket = new WebSocket(
        'ws://' + window.location.host +
        '/ws/chat/');

    chatSocket.onopen = () => {
        console.log('Connected to the chat socket');
    }

    chatSocket.onclose = () => {
        console.log('Disconnected from the chat socket');
        setTimeout(function () {
            console.log("Reconnecting...");
            connectSocket();
        }, 2000);
    }

    chatSocket.onmessage = (e) => {
        console.log('Received message from the chat socket');
        const data = JSON.parse(e.data);
        console.log(data);

        if (data['type'] === 'chat') {
            // Create HTML of message as a string
            const messageEle = '<div class="col-12">\
            <div class="row">\
                <div class="col-12">\
                    <h5><b>'+ data['name'] + '</b></h5>\
                </div>\
            </div>\
            <div class="row">\
                <div class="col-12">\
                    <p>' + data['message'] + '</p>\
                </div>\
            </div>\
        </div>'

            // Add messageEle at the bottom of the messages
            $('#chats').append(messageEle);

            // Scroll to bottom of messages
            $('#chats').scrollTop($('#chats').height());
        }
    }

    chatSocket.onerror = (e) => {
        console.log('Error from the chat socket');
        console.log(e);
        chatSocket.close();
    }
}

const addmessage = () => {
    // Get the message from the input field
    const message = message_field.value;

    if (message.length === 0) return;
    // Send the message to the server
    //Disable normal form submit behavior
    event.preventDefault();
    chatSocket.send(JSON.stringify({
        'name': sessionStorage.getItem('name'),
        'message': message
    }));
    // Clear the input field
    message_field.value = '';
}

$(document).ready(function () {
    connectSocket();
    $('#chats').scrollTop($('#chats').height());
});