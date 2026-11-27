const form = document.querySelector("#complaint-form");
const textarea = document.querySelector("#complaint");
const count = document.querySelector("#char-count");
const submit = document.querySelector("#submit-btn");
const submitLabel = document.querySelector("#submit-label");
const badge = document.querySelector("#model-badge");
const empty = document.querySelector("#result-empty");
const content = document.querySelector("#result-content");
const status = document.querySelector(".result-status");
const statusText = document.querySelector("#result-status");
const output = document.querySelector("#result-output");
const model = document.querySelector("#metric-model");
const calls = document.querySelector("#metric-calls");
const tokens = document.querySelector("#metric-tokens");
const copy = document.querySelector("#copy-btn");

let providerReady = false;
let fakeMode = false;
let busy = false;

function showResult(kind, label, message) {
  empty.hidden = true;
  content.hidden = false;
  status.className = "result-status" + (kind === "success" ? "" : " " + kind);
  statusText.textContent = label;
  output.textContent = message;
}

function setBusy(value) {
  busy = value;
  submit.disabled = value;
  textarea.readOnly = value;
  document.querySelectorAll(".example-card").forEach((button) => { button.disabled = value; });
  submitLabel.textContent = value ? "ĐANG KIỂM TRA..." : "KIỂM TRA ĐƠN HÀNG";
}

async function loadStatus() {
  try {
    const response = await fetch("/api/status", { cache: "no-store" });
    if (!response.ok) throw new Error("status");
    const data = await response.json();
    providerReady = Boolean(data.ready);
    fakeMode = data.provider === "fake";
    badge.classList.toggle("fake", !providerReady);
    badge.lastChild.textContent = providerReady ? " AI THẬT · " + data.model.toUpperCase() : fakeMode ? " CHẾ ĐỘ GIẢ · CHƯA NỐI MODEL" : " MODEL CHƯA SẴN SÀNG";
  } catch {
    badge.classList.add("fake");
    badge.lastChild.textContent = " KHÔNG KẾT NỐI";
  }
}
loadStatus();

textarea.addEventListener("input", () => {
  count.textContent = textarea.value.length;
});

for (const button of document.querySelectorAll(".example-card")) {
  button.addEventListener("click", () => {
    textarea.value = button.dataset.example || "";
    textarea.dispatchEvent(new Event("input"));
    textarea.focus();
    textarea.setSelectionRange(textarea.value.length, textarea.value.length);
    if (window.innerWidth < 780) textarea.scrollIntoView({ behavior: "smooth", block: "center" });
  });
}

textarea.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && (event.ctrlKey || event.metaKey)) {
    event.preventDefault();
    form.requestSubmit();
  }
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (busy) return;
  const text = textarea.value.trim();
  if (!text) {
    textarea.focus();
    return;
  }
  setBusy(true);
  showResult("loading", "ĐANG ĐỐI CHIẾU", "Vinflow đang đọc khiếu nại và kiểm tra thông tin đơn hàng. Vui lòng chờ trong giây lát.");
  model.textContent = "—";
  calls.textContent = "—";
  tokens.textContent = "—";
  copy.hidden = true;
  if (window.innerWidth < 780) content.scrollIntoView({ behavior: "smooth", block: "nearest" });
  try {
    const response = await fetch("/api/answer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Model chưa trả lời. Vui lòng thử lại.");
    showResult("success", providerReady ? "ĐÃ CÓ HƯỚNG XỬ LÝ" : fakeMode ? "KẾT QUẢ THỬ · MODEL GIẢ" : "KẾT QUẢ THỬ", data.output);
    model.textContent = data.model || "—";
    calls.textContent = (data.model_calls ?? 0) + " AI / " + (data.tool_calls ?? 0) + " công cụ";
    tokens.textContent = (data.tokens_in ?? 0) + " / " + (data.tokens_out ?? 0);
    copy.hidden = false;
  } catch (error) {
    showResult("error", "CHƯA THỂ XỬ LÝ", error.message || "Có lỗi kết nối. Vui lòng thử lại.");
  } finally {
    setBusy(false);
  }
});

copy.addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(output.textContent);
    copy.firstChild.textContent = "ĐÃ SAO CHÉP ";
    setTimeout(() => { copy.firstChild.textContent = "SAO CHÉP PHẢN HỒI "; }, 1800);
  } catch {
    copy.firstChild.textContent = "KHÔNG SAO CHÉP ĐƯỢC ";
    setTimeout(() => { copy.firstChild.textContent = "SAO CHÉP PHẢN HỒI "; }, 1800);
  }
});
