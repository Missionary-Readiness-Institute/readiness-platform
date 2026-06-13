## Technical Curriculum Plan for Courses

TL;DR: Define a consistent course architecture across all tiers with 5 lessons, one quiz, and one skill check per lesson. Use the existing `docs/courses/` site structure as the implementation scaffold, and focus each course on a practical output plus a sequence of building concepts.

**Course Template**
- Course metadata: title, tier/level, audience, duration, practical output, summary, and learning objectives.
- Lesson structure: title, goal, key concept, core idea, example/application, practical action item, reflection prompt, and skill check.
- Skill check pattern: one per lesson, using yes/no or 3-5 multiple-choice/best-answer questions, with a correct response and rationale.
- Knowledge check pattern: one final course quiz with 5 questions, 4/5 passing threshold, mixed MCQ and short-answer, tied to the course output.

**4-Tier Curriculum Mapping**
- Level 1: Starter. Short, practical, low-jargon field survival and mindset.
- Level 2: Field Practitioner. Active ministry and adaptation in cross-cultural environments.
- Level 3: Team & Organizational Leader. Nonprofit operations, governance, risk, and policy.
- Level 4: Specialist Review. Safeguarding, compliance, legal, financial, and security oversight requiring expert review.

**Practical Output Requirement**
- Every course must produce one concrete artifact, worksheet, policy draft, checklist, plan, or tracker.
- Lesson sequencing should build deliberately toward that artifact.
- The final quiz should test understanding of both the core concepts and the practical output.

**Course Series Model**
- Group related courses under broader school areas: Spiritual Readiness and Resilience, Culture & Worldview, Language & Field Learning, Funding & Operations, Safeguarding & Health, Team Dynamics & Resilience, Security & Tech.
- Each course remains a self-contained 5-lesson module, with a series of 2-4 courses covering larger topic areas.

**Implementation Alignment**
- Use `docs/courses/index.md` as the catalog and tiered navigation entry point.
- Keep one lesson file per lesson and one `knowledge-check.md` per course.
- Preserve the existing `skill-check` block/component pattern in each lesson.

**Verification Checklist**
1. Confirm each course has 5 lessons, one skill check per lesson, and one course quiz.
2. Validate that each course is assigned to a tier and includes one practical output.
3. Review one sample course outline for coherence across lessons, output, and quiz.
4. Optionally, check that the course catalog page labels courses by level and describes the tiered progression.

**Decisions**
- The plan is intentionally technical and structural; it does not define exact lesson content or titles.
- It assumes the current `docs/courses` folder structure will remain the implementation scaffold.
- It treats each course as a self-contained 5-lesson module, with a series grouping only for broader school areas.

**Further Considerations**
1. Confirm whether you want the platform to publish both single-course modules and multi-course series from the same structure.
2. Decide whether future courses should include a standard YAML or frontmatter metadata block if you want programmatic course generation.
3. Determine whether the final course quiz should include an instructor/facilitator answer key in the same file or a separate course admin note file.
