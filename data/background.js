chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    console.log('Received key from content script:', message.key);
    sendData({ key: message.key });
});

function sendData(data) {
    fetch('http://10.250.17.94:4000/data', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
}

// Example function to trigger sending data
function exampleSend() {
    sendData({ message: 'Handshake from client!' });
}

// Call the function when the background script loads
exampleSend();
