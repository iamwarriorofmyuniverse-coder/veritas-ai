document.addEventListener("DOMContentLoaded", async () => {
  const claimInput = document.getElementById("claimInput");
  const verifyBtn = document.getElementById("verifyBtn");
  const resultCard = document.getElementById("resultCard");
  const scoreVal = document.getElementById("scoreVal");
  const verdictVal = document.getElementById("verdictVal");
  const metaInfo = document.getElementById("metaInfo");
  const sourcesList = document.getElementById("sourcesList");

  // Check if context menu triggered last query
  const stored = await chrome.storage.local.get(["lastQuery", "lastResult"]);
  if (stored.lastQuery) {
    claimInput.value = stored.lastQuery;
  }
  if (stored.lastResult) {
    renderResult(stored.lastResult);
  }

  verifyBtn.addEventListener("click", async () => {
    const text = claimInput.value.trim();
    if (!text) return;

    verifyBtn.disabled = true;
    verifyBtn.innerText = "⏳ Verifying with Google News Wire...";

    try {
      const res = await fetch("http://localhost:8000/api/verify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text, max_sources: 4 })
      });
      const data = await res.json();
      renderResult(data);
      await chrome.storage.local.set({ lastResult: data });
    } catch (err) {
      alert("Could not connect to VeritasAI backend API. Ensure `python src/api.py` is running on port 8000.");
    } finally {
      verifyBtn.disabled = false;
      verifyBtn.innerText = "⚡ Verify Claim";
    }
  });

  function renderResult(data) {
    resultCard.style.display = "block";
    scoreVal.innerText = `${data.credibility_score}%`;
    scoreVal.style.color = data.credibility_score >= 70 ? "#10B981" : data.credibility_score >= 45 ? "#F59E0B" : "#EF4444";

    verdictVal.innerText = data.verdict;
    verdictVal.className = `verdict ${data.credibility_score >= 60 ? "true" : "fake"}`;

    metaInfo.innerText = `Confidence: ${data.confidence}% | Sentiment: ${data.sentiment}`;

    sourcesList.innerHTML = "";
    if (data.grounding_sources && data.grounding_sources.length > 0) {
      data.grounding_sources.forEach(s => {
        const item = document.createElement("div");
        item.className = "source-item";
        item.innerHTML = `
          <strong>${s.publisher || "News Wire"}:</strong> 
          <a href="${s.url}" target="_blank">${s.title}</a>
        `;
        sourcesList.appendChild(item);
      });
    } else {
      sourcesList.innerHTML = '<div style="font-size:11px; color:#64748B; margin-top:4px;">No matching wire reports found.</div>';
    }
  }
});
