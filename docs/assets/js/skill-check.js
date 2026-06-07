document.addEventListener("DOMContentLoaded", () => {
  const checks = document.querySelectorAll(".skill-check");

  checks.forEach((check, index) => {
    const question = check.dataset.question;
    const options = JSON.parse(check.dataset.options || "[]");
    const correctAnswer = Number(check.dataset.answer);
    const explanation = check.dataset.explanation || "";

    if (!question || options.length < 2 || Number.isNaN(correctAnswer)) {
      check.innerHTML = `
        <div class="skill-check-card error">
          <strong>Skill check configuration error.</strong>
        </div>
      `;
      return;
    }

    const groupName = `skill-check-${index}`;

    check.innerHTML = `
      <div class="skill-check-card">
        <div class="skill-check-label">Skill Check</div>
        <h3 class="skill-check-question">${question}</h3>

        <form class="skill-check-options">
          ${options.map((option, optionIndex) => `
            <label class="skill-check-option">
              <input type="radio" name="${groupName}" value="${optionIndex}">
              <span>${option}</span>
            </label>
          `).join("")}
        </form>

        <button type="button" class="skill-check-button">
          Check Answer
        </button>

        <div class="skill-check-result" aria-live="polite"></div>
      </div>
    `;

    const button = check.querySelector(".skill-check-button");
    const result = check.querySelector(".skill-check-result");

    button.addEventListener("click", () => {
      const selected = check.querySelector(`input[name="${groupName}"]:checked`);

      if (!selected) {
        result.className = "skill-check-result warning";
        result.textContent = "Please select an answer first.";
        return;
      }

      const selectedValue = Number(selected.value);

      if (selectedValue === correctAnswer) {
        result.className = "skill-check-result correct";
        result.innerHTML = `
          <strong>Correct.</strong>
          ${explanation ? `<p>${explanation}</p>` : ""}
        `;
      } else {
        result.className = "skill-check-result incorrect";
        result.innerHTML = `
          <strong>Not quite.</strong>
          ${explanation ? `<p>${explanation}</p>` : ""}
        `;
      }
    });
  });
});