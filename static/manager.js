var dataText = document.getElementById("data").textContent;
var dataDict = {};
let next = 0;

if (dataText.length !== 0) {
  try {
    var data = JSON.parse(dataText);
    const form = document.getElementById('main'); // Select the form element
    form.removeAttribute('action'); // Remove the action attribute
    form.removeAttribute('method'); // Remove the method attribute
    document.getElementById("asker").innerHTML = data["questions"][0];
    form.addEventListener("submit", function(event) {
      event.preventDefault(); // Prevent the form from submitting normally
      next += 1;
      if (next < data["questions"].length) {
        dataDict[data["questions"][next-1]] = form.elements['prompt'].value;
        form.elements['prompt'].value = '';
        document.getElementById("asker").innerHTML = data["questions"][next];
      } else {
        form.remove();
        document.getElementById("asker").remove();
        document.getElementById('display').textContent = "Here are your results: ";
        document.getElementById('display').style.textAlign = "center";
        body = document.getElementById("mainbody");
        let text = "";
        for (const [key, value] of Object.entries(dataDict)) {
          const p = document.createElement("p");
          p.textContent = `${key}: ${value}`;
          body.appendChild(p);
          text += `${key}: ${value}\n`;
        }
        const h1 = document.createElement("h1");
        h1.textContent = "Send these symptoms to a doctor to get a diagnosis.";
        body.appendChild(h1);
        
      }
    });
  } catch (error) {
    console.error('Error parsing data:', error);
  }
}

//Next: use the data from symptoms to generate more questions that relate to specific health problems to send to a doctor