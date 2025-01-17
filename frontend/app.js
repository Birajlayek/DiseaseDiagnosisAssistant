async function predict() {
    const symptoms = document.getElementById("symptoms").value.split(",");
    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ symptoms }),
    });
    const data = await response.json();
    document.getElementById("result").textContent = `Predicted Disease: ${data.disease}`;
}