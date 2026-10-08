// VeritasAI Content Script for on-page social feed overlay
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "SHOW_VERDICT" && message.result) {
    displayVeritasCard(message.result);
  }
});

function displayVeritasCard(data) {
  let existing = document.getElementById("veritas-ai-floating-badge");
  if (existing) existing.remove();

  const isHighRisk = data.credibility_score < 50;
  const badgeColor = isHighRisk ? "#EF4444" : "#10B981";

  const badge = document.createElement("div");
  badge.id = "veritas-ai-floating-badge";
  badge.style.cssText = `
    position: fixed;
    bottom: 24px;
    right: 24px;
    width: 340px;
    background: #0F172A;
    color: #F8FAFC;
    padding: 16px;
    border-radius: 12px;
    box-shadow: 0 12px 32px rgba(0,0,0,0.45);
    border: 1px solid rgba(255,255,255,0.1);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    z-index: 999999;
    animation: veritasSlideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  `;

  badge.innerHTML = `
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
      <div style="display: flex; align-items: center; gap: 6px;">
        <span style="font-size: 16px;">🔍</span>
        <strong style="font-size: 14px; color: #38BDF8;">VeritasAI Fact-Check</strong>
      </div>
      <button id="veritas-close-btn" style="background:none; border:none; color:#94A3B8; cursor:pointer; font-size:16px;">✕</button>
    </div>
    <div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px; margin-bottom: 10px;">
      <div style="font-size: 12px; color: #94A3B8; margin-bottom: 4px;">Verdict:</div>
      <div style="font-size: 14px; font-weight: 600; color: ${badgeColor};">${data.verdict}</div>
      <div style="font-size: 12px; margin-top: 6px; color: #CBD5E1;">
        Credibility Score: <strong>${data.credibility_score}%</strong> (Confidence: ${data.confidence}%)
      </div>
    </div>
    ${data.grounding_sources && data.grounding_sources.length > 0 ? `
      <div style="font-size: 11px; color: #94A3B8; margin-bottom: 4px;">Live Grounding Source:</div>
      <a href="${data.grounding_sources[0].url}" target="_blank" style="display:block; font-size: 11px; color: #38BDF8; text-decoration: none; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
        🔗 ${data.grounding_sources[0].title}
      </a>
    ` : '<div style="font-size: 11px; color: #64748B;">No live matching wire articles found.</div>'}
  `;

  document.body.appendChild(badge);

  document.getElementById("veritas-close-btn").onclick = () => {
    badge.remove();
  };
}
