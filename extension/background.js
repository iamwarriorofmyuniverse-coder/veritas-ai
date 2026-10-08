// VeritasAI Background Service Worker (Manifest V3)
chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "veritas-fact-check",
    title: "🔍 Fact-Check with VeritasAI",
    contexts: ["selection"]
  });
});

chrome.contextMenus.onClicked.addListener(async (info, tab) => {
  if (info.menuItemId === "veritas-fact-check" && info.selectionText) {
    const selectedText = info.selectionText.trim();
    
    // Save query to storage so popup or content script can display immediately
    await chrome.storage.local.set({ lastQuery: selectedText, isChecking: true });

    try {
      const response = await fetch("http://localhost:8000/api/verify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: selectedText, max_sources: 5 })
      });
      const data = await response.json();
      await chrome.storage.local.set({ lastResult: data, isChecking: false });
      
      // Notify content script to display in-page pill/modal
      if (tab.id) {
        chrome.tabs.sendMessage(tab.id, {
          action: "SHOW_VERDICT",
          result: data
        });
      }
    } catch (err) {
      console.error("VeritasAI verification error:", err);
      await chrome.storage.local.set({
        lastResult: {
          verdict: "Error reaching VeritasAI backend (is server running on port 8000?)",
          credibility_score: 0,
          confidence: 0,
          sentiment: "Unknown",
          grounding_sources: []
        },
        isChecking: false
      });
    }
  }
});
