async function uploadResume() {
  const fileInput = document.getElementById("resumeFile");
  const status = document.getElementById("uploadStatus");

  if (!fileInput.files.length) {
    status.innerText = "Please select a PDF file.";
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  status.innerText = "Uploading and analyzing resume...";

  try {
    const response = await fetch("http://127.0.0.1:8000/analyze-resume", {
      method: "POST",
      body: formData
    });

    if (!response.ok) throw new Error("Upload failed");

    status.innerText = "Resume analyzed successfully ✅";

    loadDashboard();
    loadExplanations();

  } catch (err) {
    status.innerText = "Error analyzing resume ❌";
  }
}

async function loadDashboard() {
  const response = await fetch("http://127.0.0.1:8000/dashboard");
  const data = await response.json();

  document.getElementById("totalResumes").innerText =
    data.total_resumes_analyzed;

  new Chart(document.getElementById("rejectionChart"), {
    type: "bar",
    data: {
      labels: data.top_rejection_reasons.map(r => r[0]),
      datasets: [{
        label: "Rejections",
        data: data.top_rejection_reasons.map(r => r[1]),
        backgroundColor: "#ef4444"
      }]
    }
  });

  new Chart(document.getElementById("biasChart"), {
    type: "bar",
    data: {
      labels: data.bias_trends.map(b => b[0]),
      datasets: [{
        label: "Bias Flags",
        data: data.bias_trends.map(b => b[1]),
        backgroundColor: "#f59e0b"
      }]
    }
  });

  new Chart(document.getElementById("skillsChart"), {
    type: "pie",
    data: {
      labels: data.top_detected_skills.map(s => s[0]),
      datasets: [{
        data: data.top_detected_skills.map(s => s[1]),
        backgroundColor: [
          "#2563eb",
          "#22c55e",
          "#a855f7",
          "#ec4899",
          "#14b8a6"
        ]
      }]
    }
  });
}

async function loadExplanations() {
  const response = await fetch("http://127.0.0.1:8000/explanations");
  const data = await response.json();

  const container = document.getElementById("explanationList");
  container.innerHTML = "";

  data.explanations.forEach(text => {
    const div = document.createElement("div");
    div.className = "explanation-card";
    div.innerText = text;
    container.appendChild(div);
  });
}

// Initial load
loadDashboard();
loadExplanations();
