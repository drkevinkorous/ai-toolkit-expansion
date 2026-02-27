const STORAGE_KEY = "ai_toolkit_weekly_tracker";
const THEME_KEY = "ai_toolkit_theme_preference";
const AUTH_USER_KEY = "ai_toolkit_auth_user";
const AUTH_SALT_KEY = "ai_toolkit_auth_salt";
const AUTH_HASH_KEY = "ai_toolkit_auth_hash";
const AUTH_SESSION_KEY = "ai_toolkit_auth_session";
const AUTH_MODE_DEFAULT = "login";

const defaultWeeks = [
  {
    id: 1,
    week: "Week 1",
    task: "The Vibe Code Kickoff: Build Your Resolution Tracker",
    complete: false,
    notes: "",
    hours: "",
    completedAt: "",
    work: [
      "Build it: Use Replit Agent, Lovable, or Cursor to create a simple tracker app.",
      "Core Features: List of all 10 weekends, completion checkboxes, notes field, progress bar.",
      "Ship it: Deploy live (Most vibe coding tools have features for this now).",
      "Use it: Log Weekend 1 as \"Complete\" before closing laptop.",
    ],
    advanced: [
      "Add user authentication for multi-user support.",
      "Build as a PWA for mobile access.",
      "Add \"suggest next weekend\" logic.",
      "Add time-tracking field.",
    ],
  },
  {
    id: 2,
    week: "Week 2",
    task: "The Model Mapping Project: Build Your Personal AI Topography",
    complete: false,
    notes: "",
    hours: "",
    completedAt: "",
    work: [
      "Pick 2-3 models: Use what you have (Claude, ChatGPT, Gemini).",
      "Run tests: Run the same task through each: Deep Research, Writing, Strategy, Data, Visual.",
      "Compare: Which felt right? Which was faster? Which asked better questions?",
      "Synthesize: Create a one-page \"Rules of Thumb\" (e.g., \"Claude for drafts, ChatGPT for code\").",
    ],
    advanced: [
      "Test specialized tools (Perplexity, etc.).",
      "Build a matrix including cost and context window.",
      "Test output consistency over time.",
      "Track editing time needed per model.",
    ],
  },
  {
    id: 3,
    week: "Week 3",
    task: "The Deep Research Sprint: Let AI Do a Week's Research in an Afternoon",
    complete: false,
    notes: "",
    hours: "",
    completedAt: "",
    work: [
      "Real question: Pick a decision you actually need to make (not hypothetical).",
      "Deep tools: Use Claude, Gemini, or ChatGPT deep research modes.",
      "Iterate: Push back. Ask for disconfirming evidence. Do not accept first output.",
      "Structure: Problem, Findings, Options, Recommendation, Risks.",
    ],
    advanced: [
      "Run the same question through all 3 major tools.",
      "Create a meta-analysis of which tool was most accurate.",
      "Build a \"Fact Check List\" of 10 claims you verify manually.",
    ],
  },
  {
    id: 4,
    week: "Week 4",
    task: "The Analysis Project: Turn Messy Data Into Actual Decisions",
    complete: false,
    notes: "",
    hours: "",
    completedAt: "",
    work: [
      "Collect: Gather real data (CSV/spreadsheet) from Spotify, bank, Google Takeout, or Kaggle.",
      "Upload: Use Claude or ChatGPT to propose cleaning steps, 5-10 metrics, and 3 hypotheses.",
      "Produce: Cleaned dataset, summary table, 3 insights, 3 actions.",
      "Write: A one-page Insights Memo (no charts required).",
    ],
    advanced: [
      "Build a reusable prompt template for monthly updates.",
      "Connect to a live data source for real-time analysis.",
      "Compare insights from Claude vs. ChatGPT on the same data.",
    ],
  },
  {
    id: 5,
    week: "Week 5",
    task: "The Visual Reasoning Project: Make AI See and Think",
    complete: false,
    notes: "",
    hours: "",
    completedAt: "",
    work: [
      "Concept: Pick a process, comparison, framework, or timeline.",
      "Reasoning: Ask AI \"What is the best logic to visualize this? What are the tradeoffs?\"",
      "Draft: Generate 2 alternate design approaches (e.g., flowchart vs matrix).",
      "Finalize: Build it using AI generation or tools like Canva/Gamma.",
      "Visual QA: Readable in 5s? One clear takeaway?",
    ],
    advanced: [
      "Create a reusable visual system or template.",
      "Design and build a complex data visualization.",
      "Build a visual pattern library (2x2s, cycles, flows).",
    ],
  },
  {
    id: 6,
    week: "Week 6",
    task: "The Information Pipeline: Build Your NotebookLM + Gamma Stack",
    complete: false,
    notes: "",
    hours: "",
    completedAt: "",
    work: [
      "Input: Take a corpus (transcript, report, notes, or book).",
      "NotebookLM: Generate summary, glossary, FAQ, and audio overview.",
      "Gamma: Create 8-12 slide deck with 1 visual and clear recommendation.",
      "Document: Save the prompts and workflow to repeat later.",
    ],
    advanced: [
      "Build full repurposing pipeline (audio, deck, one-pager, tweets).",
      "Time the process and compare to manual effort.",
      "Create a reusable checklist template.",
    ],
  },
  {
    id: 7,
    week: "Week 7",
    task: "The First Automation: Build Your Content Distribution Machine",
    complete: false,
    notes: "",
    hours: "",
    completedAt: "",
    work: [
      "Components: Must have Trigger, Transform, Route, Approval, and Logging.",
      "Tools: Use Lindy, n8n, Make, or native Slack/Notion workflows.",
      "Build: Example, Notion note -> Summarize -> Draft tweets -> Send to Slack.",
      "Default: Weekly Reading Digest (summarize saved links, email digest).",
    ],
    advanced: [
      "Chain multiple automations together.",
      "Add conditional logic for different content types.",
      "Add robust error handling for failures.",
      "Log detailed analytics.",
    ],
  },
  {
    id: 8,
    week: "Week 8",
    task: "The Second Automation: Build Your Productivity Workflow",
    complete: false,
    notes: "",
    hours: "",
    completedAt: "",
    work: [
      "Components: Trigger -> Transform -> Route -> Approval -> Logging.",
      "Pick one: Inbox -> Follow-up OR Lead -> Response OR Meeting Prep Bot.",
      "Default: Prep Bot (calendar event -> LinkedIn lookup + history check -> briefing sent 30m before).",
      "Platform: Use Lindy, n8n, Make, or Zapier.",
    ],
    advanced: [
      "Add a feedback loop to rate output quality.",
      "Make it conversational (e.g., Slack bot drafts reply, you say \"send\").",
      "Connect to CRM/tracker for dashboard view.",
    ],
  },
  {
    id: 9,
    week: "Week 9",
    task: "The Context Engineering Project: Build Your Personal AI Operating System",
    complete: false,
    notes: "",
    hours: "",
    completedAt: "",
    work: [
      "AI OS structure: Create sections in Notion/Obsidian: Playbook, Artifacts Library, Automation Log, and Decisions Log.",
      "Capture habit: Set up one central inbox for AI notes and a 15-minute weekly review.",
      "Context Doc: Write your role, key projects, style preferences, and a \"What to Avoid\" list.",
      "Deploy: Save the Context Doc where you can copy-paste it instantly.",
    ],
    advanced: [
      "Create multiple context profiles (e.g., separate Work vs. Personal).",
      "Include actual examples of your writing/emails in the context file.",
      "Build a quarterly context refresh into your calendar.",
    ],
  },
  {
    id: 10,
    week: "Week 10",
    task: "The AI-Powered Build: Build Something With AI Inside It",
    complete: false,
    notes: "",
    hours: "",
    completedAt: "",
    work: [
      "Platform: Use Google AI Studio or similar to build the core logic.",
      "Option A (Knowledge): Build a chatbot trained on your expertise, notes, or FAQs.",
      "Option B (Voice): Build a voice agent for practice (language, interviews, sales).",
      "Option C (Mini-Agent): Ingest docs -> extract info -> output structured data.",
      "Deploy: Ship it somewhere usable, even if just for yourself.",
    ],
    advanced: [
      "Build something for others (team/clients), not just you.",
      "Train it on a specific company knowledge base.",
      "Give it to real people, get feedback, and iterate.",
      "Move from \"side project\" to \"prototype\".",
    ],
  },
];

const weeksContainer = document.getElementById("weeks");
const progressFill = document.getElementById("progressFill");
const progressText = document.getElementById("progressText");
const hoursText = document.getElementById("hoursText");
const resetButton = document.getElementById("resetButton");
const themeSelect = document.getElementById("themeSelect");
const prevButton = document.getElementById("prevButton");
const nextButton = document.getElementById("nextButton");
const navStatus = document.getElementById("navStatus");
const prefersDark = window.matchMedia("(prefers-color-scheme: dark)");
const authOverlay = document.getElementById("authOverlay");
const authTitle = document.getElementById("authTitle");
const authSubtitle = document.getElementById("authSubtitle");
const authForm = document.getElementById("authForm");
const authUsername = document.getElementById("authUsername");
const authPassword = document.getElementById("authPassword");
const authMessage = document.getElementById("authMessage");
const lockButton = document.getElementById("lockButton");
const changePasswordButton = document.getElementById("changePasswordButton");
const exportButton = document.getElementById("exportButton");

let currentIndex = 0;
let appStarted = false;
let authMode = AUTH_MODE_DEFAULT;

const mergeWeek = (stored, fallback) => {
  const normalized = stored || {};
  return {
    ...fallback,
    ...normalized,
    task:
      typeof normalized.task === "string" &&
      normalized.task.trim() &&
      !/^Task\s+\d+/i.test(normalized.task.trim())
        ? normalized.task
        : fallback.task,
    completedAt:
      typeof normalized.completedAt === "string" ? normalized.completedAt : "",
    work:
      Array.isArray(normalized.work) && normalized.work.length
        ? normalized.work
        : fallback.work,
    advanced:
      Array.isArray(normalized.advanced) && normalized.advanced.length
        ? normalized.advanced
        : fallback.advanced,
  };
};

const loadWeeks = () => {
  const stored = localStorage.getItem(STORAGE_KEY);
  if (!stored) {
    return defaultWeeks;
  }
  try {
    const parsed = JSON.parse(stored);
    if (Array.isArray(parsed) && parsed.length === 10) {
      return parsed.map((item, index) => mergeWeek(item, defaultWeeks[index]));
    }
    return defaultWeeks;
  } catch (error) {
    return defaultWeeks;
  }
};

const saveWeeks = (weeks) => {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(weeks));
};

const toHex = (buffer) => {
  const bytes = new Uint8Array(buffer);
  return Array.from(bytes)
    .map((byte) => byte.toString(16).padStart(2, "0"))
    .join("");
};

const hashPassword = async (password, salt) => {
  const encoded = new TextEncoder().encode(`${salt}${password}`);
  const digest = await crypto.subtle.digest("SHA-256", encoded);
  return toHex(digest);
};

const generateSalt = () => {
  const bytes = new Uint8Array(16);
  crypto.getRandomValues(bytes);
  return toHex(bytes);
};

const hasAuthConfig = () =>
  Boolean(
    localStorage.getItem(AUTH_USER_KEY) &&
      localStorage.getItem(AUTH_SALT_KEY) &&
      localStorage.getItem(AUTH_HASH_KEY)
  );

const setAuthMessage = (message) => {
  if (authMessage) {
    authMessage.textContent = message;
  }
};

const showAuthOverlay = (mode) => {
  if (!authOverlay) {
    return;
  }
  authMode = mode;
  authOverlay.classList.add("is-visible");
  authOverlay.setAttribute("aria-hidden", "false");
  const isSetup = mode === "setup" || mode === "reset";
  if (authTitle && authSubtitle) {
    if (mode === "reset") {
      authTitle.textContent = "Change credentials";
      authSubtitle.textContent = "Set a new username and password for this browser.";
    } else {
      authTitle.textContent = isSetup ? "Create local login" : "Sign in";
      authSubtitle.textContent = isSetup
        ? "Set a username and password for this browser."
        : "Enter your credentials to continue.";
    }
  }
  if (authPassword) {
    authPassword.value = "";
  }
  setAuthMessage("");
};

const hideAuthOverlay = () => {
  if (!authOverlay) {
    return;
  }
  authOverlay.classList.remove("is-visible");
  authOverlay.setAttribute("aria-hidden", "true");
};

const getEffectiveTheme = (choice) => {
  if (choice === "dark" || choice === "light") {
    return choice;
  }
  return prefersDark.matches ? "dark" : "light";
};

const applyTheme = (choice) => {
  const effective = getEffectiveTheme(choice);
  if (effective === "dark") {
    document.body.dataset.theme = "dark";
  } else {
    delete document.body.dataset.theme;
  }
};

const loadTheme = () => {
  const stored = localStorage.getItem(THEME_KEY) || "system";
  if (themeSelect) {
    themeSelect.value = stored;
  }
  applyTheme(stored);
};

const setupThemeHandlers = () => {
  if (themeSelect) {
    themeSelect.addEventListener("change", () => {
      const choice = themeSelect.value;
      localStorage.setItem(THEME_KEY, choice);
      applyTheme(choice);
    });
  }
  prefersDark.addEventListener("change", () => {
    if (localStorage.getItem(THEME_KEY) === "system") {
      applyTheme("system");
    }
  });
};

const updateProgress = (weeks) => {
  const completed = weeks.filter((week) => week.complete).length;
  const percent = Math.round((completed / weeks.length) * 100);
  progressFill.style.width = `${percent}%`;
  progressText.textContent = `${percent}% complete`;

  const totalHours = weeks.reduce((sum, week) => {
    const value = parseFloat(week.hours);
    return Number.isFinite(value) ? sum + value : sum;
  }, 0);
  hoursText.textContent = `${totalHours.toFixed(1)} hours logged`;
};

const csvEscape = (value) => {
  const text = String(value ?? "");
  if (/[",\n]/.test(text)) {
    return `"${text.replace(/"/g, '""')}"`;
  }
  return text;
};

const handleExport = () => {
  const weeks = loadWeeks();
  const rows = [
    ["Task Title", "Notes", "Time Spent (hours)", "Date Completed"],
    ...weeks.map((week) => [
      week.task,
      week.notes,
      week.hours,
      week.completedAt || "",
    ]),
  ];
  const csv = rows.map((row) => row.map(csvEscape).join(",")).join("\n");
  const blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = "ai-weekly-tracker.csv";
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
};

const createDetailsSection = (label, items) => {
  const section = document.createElement("div");
  section.className = "details-section";

  const title = document.createElement("div");
  title.className = "details-title";
  title.textContent = label;

  const list = document.createElement("ul");
  list.className = "details-list";

  items.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    list.appendChild(li);
  });

  section.appendChild(title);
  section.appendChild(list);

  return section;
};

const createCard = (week, weeks) => {
  const card = document.createElement("article");
  card.className = "card";

  const header = document.createElement("div");
  header.className = "card-header";

  const title = document.createElement("div");
  title.className = "card-title";
  title.textContent = week.task;

  const subtitle = document.createElement("div");
  subtitle.className = "card-subtitle";
  subtitle.textContent = week.week;

  const checkboxLabel = document.createElement("label");
  checkboxLabel.className = "checkbox";

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.checked = week.complete;
  checkbox.addEventListener("change", () => {
    week.complete = checkbox.checked;
    week.completedAt = checkbox.checked
      ? new Date().toISOString().slice(0, 10)
      : "";
    saveWeeks(weeks);
    updateProgress(weeks);
  });

  const checkboxText = document.createElement("span");
  checkboxText.textContent = "Complete";

  checkboxLabel.appendChild(checkbox);
  checkboxLabel.appendChild(checkboxText);

  const titleBlock = document.createElement("div");
  titleBlock.appendChild(title);
  titleBlock.appendChild(subtitle);

  header.innerHTML = "";
  header.appendChild(titleBlock);
  header.appendChild(checkboxLabel);

  const details = document.createElement("div");
  details.className = "details";
  details.appendChild(createDetailsSection("The Work", week.work));
  details.appendChild(createDetailsSection("Advanced", week.advanced));

  const notesField = document.createElement("label");
  notesField.className = "field";
  notesField.textContent = "Notes";

  const notesArea = document.createElement("textarea");
  notesArea.value = week.notes;
  notesArea.placeholder = "Capture what you learned or produced";
  notesArea.addEventListener("input", () => {
    week.notes = notesArea.value;
    saveWeeks(weeks);
  });

  notesField.appendChild(notesArea);

  const hoursField = document.createElement("label");
  hoursField.className = "field";
  hoursField.textContent = "Time Spent (hours)";

  const hoursInput = document.createElement("input");
  hoursInput.type = "number";
  hoursInput.min = "0";
  hoursInput.step = "0.25";
  hoursInput.placeholder = "0";
  hoursInput.value = week.hours;
  hoursInput.addEventListener("input", () => {
    week.hours = hoursInput.value;
    saveWeeks(weeks);
    updateProgress(weeks);
  });

  hoursField.appendChild(hoursInput);

  card.appendChild(header);
  card.appendChild(details);
  card.appendChild(notesField);
  card.appendChild(hoursField);

  return card;
};

const renderWeek = (weeks) => {
  const safeIndex = Math.min(Math.max(currentIndex, 0), weeks.length - 1);
  currentIndex = safeIndex;
  weeksContainer.innerHTML = "";
  const card = createCard(weeks[currentIndex], weeks);
  weeksContainer.appendChild(card);
  if (navStatus) {
    navStatus.textContent = `Week ${currentIndex + 1}`;
  }
  if (prevButton) {
    prevButton.disabled = currentIndex === 0;
  }
  if (nextButton) {
    nextButton.disabled = currentIndex === weeks.length - 1;
  }
};

const init = () => {
  const weeks = loadWeeks();
  renderWeek(weeks);
  updateProgress(weeks);
};

const startApp = () => {
  if (appStarted) {
    return;
  }
  appStarted = true;
  init();
};

if (resetButton) {
  resetButton.addEventListener("click", () => {
    localStorage.removeItem(STORAGE_KEY);
    init();
  });
}

if (prevButton) {
  prevButton.addEventListener("click", () => {
    const weeks = loadWeeks();
    currentIndex = Math.max(currentIndex - 1, 0);
    renderWeek(weeks);
  });
}

if (nextButton) {
  nextButton.addEventListener("click", () => {
    const weeks = loadWeeks();
    currentIndex = Math.min(currentIndex + 1, weeks.length - 1);
    renderWeek(weeks);
  });
}

if (lockButton) {
  lockButton.addEventListener("click", () => {
    sessionStorage.removeItem(AUTH_SESSION_KEY);
    showAuthOverlay("login");
  });
}

if (changePasswordButton) {
  changePasswordButton.addEventListener("click", () => {
    sessionStorage.removeItem(AUTH_SESSION_KEY);
    showAuthOverlay("reset");
  });
}

if (exportButton) {
  exportButton.addEventListener("click", handleExport);
}

loadTheme();
setupThemeHandlers();

if (authForm) {
  authForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const username = authUsername ? authUsername.value.trim() : "";
    const password = authPassword ? authPassword.value : "";
    if (!username || !password) {
      setAuthMessage("Please enter a username and password.");
      return;
    }
    if (!hasAuthConfig() || authMode === "reset") {
      const salt = generateSalt();
      const hash = await hashPassword(password, salt);
      localStorage.setItem(AUTH_USER_KEY, username);
      localStorage.setItem(AUTH_SALT_KEY, salt);
      localStorage.setItem(AUTH_HASH_KEY, hash);
      sessionStorage.setItem(AUTH_SESSION_KEY, "true");
      hideAuthOverlay();
      startApp();
      return;
    }
    const storedUser = localStorage.getItem(AUTH_USER_KEY);
    const storedSalt = localStorage.getItem(AUTH_SALT_KEY) || "";
    const storedHash = localStorage.getItem(AUTH_HASH_KEY) || "";
    if (storedUser !== username) {
      setAuthMessage("Username or password is incorrect.");
      return;
    }
    const hash = await hashPassword(password, storedSalt);
    if (hash !== storedHash) {
      setAuthMessage("Username or password is incorrect.");
      return;
    }
    sessionStorage.setItem(AUTH_SESSION_KEY, "true");
    hideAuthOverlay();
    startApp();
  });
}

if (sessionStorage.getItem(AUTH_SESSION_KEY) === "true") {
  hideAuthOverlay();
  startApp();
} else if (hasAuthConfig()) {
  showAuthOverlay("login");
} else {
  showAuthOverlay("setup");
}
