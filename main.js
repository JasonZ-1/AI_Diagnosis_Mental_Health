prompt_count = 0
next = null

document.getElementById("submit").addEventListener("click", collect_message);

function collect_message() {
    var message = document.getElementById("message").value;
    document.getElementById("message").value = "";

    if (prompt_count == 0) {
        console.log(message)
        const spawn = require("child_process").spawn;
        const pythonProcess = spawn('python', ["chatbot_predictor/bot.py", message]);
    }
}