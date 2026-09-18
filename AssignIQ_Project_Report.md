# AssignIQ - Educational Management System
## IDP PROJECT REPORT

**Submitted By:**
[Your Name / Team Members]

**Under the guidance of:**
[Guide Name]

**Abstract:**
The rapid evolution of digital education has significantly transformed the way educational institutions manage assignments, evaluations, and student-teacher interactions. Educational Management Systems have emerged as a crucial component in enabling seamless communication between educators and students. However, existing systems often suffer from inefficiencies such as lack of automated grading, poor plagiarism detection, complex user interfaces, and limited support for coding assignments. This project presents AssignIQ, a scalable and efficient Educational Management System designed to address these challenges through a user-centric and modular architecture. The primary motivation behind this work is to create a system that enhances educational efficiency while ensuring security, usability, and advanced AI integration. The methodology involves designing a full-stack web and mobile application using modern technologies (MERN stack, React Native), incorporating features such as role-based authentication, AI-powered assignment evaluation, multi-pass text extraction with OCR, real-time messaging, and an integrated CodeGen IDE. Experimental evaluation demonstrates improved system performance, reduced grading time, and enhanced user experience compared to traditional educational platforms.

---

### 1. INTRODUCTION

#### 1.1 Overview of the Project
The AssignIQ project is a technology-driven initiative aimed at transforming conventional educational management into a more efficient, transparent, and intelligent digital ecosystem. In traditional systems, assigning tasks, grading, and tracking student progress involve manual processes and fragmented communication, reducing efficiency and increasing the burden on educators. AssignIQ introduces a centralized educational platform that connects teachers and students directly through web and mobile applications. This integration allows institutions to manage class sections, assignments, real-time messaging, and code execution in a streamlined manner. The platform emphasizes AI-driven evaluation (with automatic grading and originality checking), real-time data access, and a user-friendly CodeGen IDE, enabling stakeholders to perform educational tasks quickly and accurately.

#### 1.2 Motivation
Despite technological advancements, many educational institutions still rely on:
- Manual grading systems
- Fragmented communication channels (email/WhatsApp)
- Inefficient plagiarism checking
This leads to:
- Delays in grading and feedback
- Lack of transparency in student performance
- Increased workload for teachers
The motivation of AssignIQ is to:
- Digitize and automate the assignment workflow
- Improve efficiency and transparency with AI-driven insights
- Provide an integrated IDE for computer science students

#### 1.3 Problem Statement
A large portion of the educational sector continues to face challenges related to inefficient assignment management and grading. Teachers often lack intelligent tools for quick plagiarism checks and automated evaluations, affecting their productivity. Students face limitations in receiving immediate feedback and accessing a unified platform for both theoretical assignments and coding tasks. Additionally, the absence of integrated real-time communication systems results in poor coordination and delays in resolving student queries. These issues highlight the need for a comprehensive digital platform like AssignIQ.

#### 1.4 Research Gaps
- Lack of intelligent, AI-driven pre-checks for assignments before final submission.
- Limited platforms offering an integrated, professional full-screen IDE for coding assignments within the same ecosystem.
- Absence of mandatory verification quizzes (MCQs and long-form) dynamically generated based on the submitted content.
- Poor integration between theoretical submissions (documents/photos with OCR) and coding environments.

#### 1.5 Objectives of the Project
- Develop a full-stack educational management platform connecting teachers, students, and admins.
- Implement AI-driven assignment evaluation to reduce manual grading efforts.
- Provide a robust CodeGen IDE with backend Piston API integration for Python, Java, JavaScript, C, and C++.
- Integrate a mandatory 10-minute AI-generated verification quiz upon assignment submission.
- Enable high-accuracy document and photo uploads with a multi-pass text extraction engine (OCR fallback).
- Facilitate real-time messaging with group chat and file sharing.

#### 1.6 Scope of the Project
The scope of AssignIQ encompasses the development of web and mobile applications supporting role-based access. It includes section management, assignment tracking, an integrated code compiler, and secure authentication (Email/Password + Google OAuth). The system handles real-time messaging via Socket.io and utilizes OpenAI for dynamic quiz generation and plagiarism detection. 

#### 1.7 Constraints
- **Cost & API Quotas**: Dependence on OpenAI and Piston API quotas; requires efficient fallback mechanisms (e.g., intelligent mock questions when AI limits are reached).
- **Usability**: Must provide a simple and intuitive UI/UX for non-technical users while supporting advanced IDE features for CS students.
- **Security**: Protection of student data, assignment submissions, and secure code execution in sandboxed environments.

#### 1.8 Benefits of the Proposed System
Reduces grading time for teachers through AI evaluations. Enhances student learning with immediate AI Precheck feedback and verification quizzes. Provides a centralized, robust platform eliminating the need for separate messaging and coding tools.

---

### 2. RELATED WORK
Existing learning management systems (LMS) like Google Classroom and Canvas provide solid assignment tracking but lack native AI-driven grading, advanced OCR for scanned documents, and built-in professional CodeGen IDEs. Many platforms require third-party integrations for plagiarism detection and coding tasks, increasing complexity and cost. 

---

### 3. PROPOSED METHODOLOGY

#### 3.1 Proposed Work Flow
1. **User Registration & Roles:** Admin approves Teachers; Teachers create Sections and add Students.
2. **Assignment Creation:** Teacher posts assignments with deadlines and criteria.
3. **Submission Precheck:** Student uploads document/photo. Multi-pass text extraction (with OCR) processes the content. AI Precheck provides feedback.
4. **Final Submission:** AI generates a mandatory 10-minute verification quiz (5 MCQs, 1 long-form) based on extracted content.
5. **Evaluation:** AI evaluates the submission and quiz. Teacher reviews the AI-generated report and finalizing grades.
6. **CodeGen:** For coding tasks, students use the built-in IDE (hybrid light/dark theme) to compile and test code via Piston API.

#### 3.2 Major Architecture
- **Frontend Layer:** React.js (Web) and React Native (Mobile), Redux Toolkit, Tailwind CSS, Material-UI.
- **Backend Layer:** Node.js, Express.js. Handles business logic, AI interactions, and real-time sockets.
- **Database Layer:** MongoDB with Mongoose for structured storage of users, submissions, and messages.
- **API Integrations:** OpenAI API (Evaluation & Quizzes), Piston API (Code Compilation), Socket.io (Real-time Chat).

---

### 4. SOFTWARE REQUIREMENT ANALYSIS

#### 4.1 Functional Requirements
- Role-based login and Google OAuth integration.
- Teacher dashboard for section and assignment management.
- Student dashboard for tracking deadlines, submitting assignments, and viewing performance.
- Document and image upload with multi-pass OCR extraction.
- AI Precheck and dynamic quiz generation system.
- Full-screen CodeGen IDE supporting 5 languages.
- Real-time WhatsApp-style messaging for class groups.

#### 4.2 Non-Functional Requirements
- **Scalability:** Ability to handle concurrent students taking quizzes or compiling code.
- **Performance:** Fast OCR extraction and low-latency code compilation.
- **Security:** Sandboxed code execution, JWT-based secure authentication.

---

### 5. CONCLUSION AND FUTURE SCOPE
AssignIQ successfully addresses the limitations of traditional LMS platforms by integrating AI-driven evaluations, an advanced OCR submission pipeline, and a professional CodeGen IDE. Future scope includes expanding the mobile application capabilities, adding predictive analytics for student performance, and integrating more advanced AI models for deeper code review and tutoring functionalities.
