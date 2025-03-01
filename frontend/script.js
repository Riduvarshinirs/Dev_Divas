function generateIdea() {
    const skills = document.getElementById("skills").value;
    const interests = document.getElementById("interests").value;
    const budget = document.getElementById("budget").value;

    fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ skills, interests, budget })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not OK");
        }
        return response.json();
    })
    .then(data => {
        console.log("API Response:", data); // Debugging: Check what API returns
        document.getElementById("output").innerText = "Startup Idea: " + (data.idea || data.startup_idea || "No idea generated");
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("output").innerText = "Error generating startup idea. Please try again.";
    });
}
