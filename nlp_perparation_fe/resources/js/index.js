document.addEventListener('DOMContentLoaded', function () {
    // Attach the click event to the button
    console.log("hello");
    document.getElementById('cleanButton').addEventListener('click', cleanText);
});


async function cleanText() {
    let text = document.getElementById("text").value;
    let source = document.getElementById("source").value;

    // Show loading text while waiting for response
    document.getElementById("output").innerText = "Cleaning... Please wait.";

    try {
        let response = await fetch("/clean", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text, source })
        });

        let result = await response.json();
        if (response.ok) {
            document.getElementById("output").innerText = result.cleaned_text || result.error;
        } else {
            document.getElementById("output").innerText = "Error: " + result.error;
        }
    } catch (error) {
        document.getElementById("output").innerText = "An error occurred while cleaning the text.";
    }
}
