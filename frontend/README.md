# EduLink SL — Frontend

A modern tutor booking marketplace for Sri Lankan O/L, A/L, and university students. Built with SvelteKit, featuring role-based dashboards for students, teachers, and administrators.

## Overview

EduLink SL connects students with verified tutors across Sri Lanka. The platform supports:
- **Students**: Browse tutors, book sessions, track progress, and access AI career guidance
- **Teachers**: Manage listings, set availability, track earnings, and communicate with students
- **Admin**: Monitor platform analytics, approve teacher verifications, and manage disputes

## Tech Stack

- **Framework**: SvelteKit 2.57.0 with Svelte 5.55.2 (using runes: `$state`, `$derived`, `$effect`)
- **Language**: TypeScript 6.0.2 (strict mode enabled)
- **Styling**: Tailwind CSS 4.2.2 with custom design tokens
- **Icons**: Lucide Svelte 1.17.0
- **Data Fetching**: TanStack Svelte Query 6.1.33
- **Validation**: Zod 4.4.3
- **UI Components**: bits-ui 2.18.1 (shadcn-svelte compatible)
- **Build Tool**: Vite 8.0.7

## Features

### Implemented
- **Public Pages**: Landing page, Find Tutors, Streams, Career Guidance
- **Authentication**: Login and registration with role selection (Student, Teacher, Admin)
- **Student Dashboard**: Welcome bar, stats, upcoming sessions, notifications, AI career chat teaser
- **Teacher Dashboard**: Earnings hero, stats, today's classes, quick actions
- **Admin Dashboard**: Platform analytics, KPI cards, monthly bookings chart, top tutors, activity feed
- **Role-based Routing**: Automatic redirection to appropriate dashboard based on user role
- **Responsive Design**: Mobile-friendly layouts with custom CSS variables

### In Progress
- Teacher verification flow
- Booking system with Stripe integration
- Real-time messaging with WebSocket
- AI career chat integration
- Payment processing

## Project Structure

```
frontend/
├── src/
│   ├── app.html              # HTML template
│   ├── app.d.ts              # TypeScript declarations
│   ├── lib/
│   │   ├── api/              # API client and endpoint definitions
│   │   │   └── client.ts     # Base fetch wrapper with auth headers
│   │   ├── assets/           # Static assets (images, fonts)
│   │   ├── components/       # Reusable Svelte components (to be populated)
│   │   │   └── ui/           # shadcn-svelte components
│   │   ├── schemas/          # Zod validation schemas (to be populated)
│   │   ├── stores/           # Svelte 5 rune stores
│   │   │   └── auth.svelte.ts # Authentication state management
│   │   ├── types/            # TypeScript type definitions
│   │   ├── utils/            # Utility functions
│   │   │   └── dates.ts      # Date formatting helpers
│   │   └── index.ts          # Library entry point
│   ├── routes/               # SvelteKit file-based routing
│   │   ├── +layout.svelte    # Root layout (loads auth state)
│   │   ├── +layout.ts        # Root load function
│   │   ├── +page.svelte      # Landing page (index)
│   │   ├── layout.css        # Global styles and CSS variables
│   │   ├── auth/             # Authentication routes
│   │   │   ├── login/
│   │   │   │   └── +page.svelte
│   │   │   └── register/
│   │   │       └── +page.svelte
│   │   ├── student/          # Student routes (role-based)
│   │   │   ├── +layout.svelte # Student sidebar layout
│   │   │   ├── dashboard/
│   │   │   │   └── +page.svelte
│   │   │   ├── bookings/     # (to be implemented)
│   │   │   ├── messages/     # (to be implemented)
│   │   │   └── ai-chat/      # (to be implemented)
│   │   ├── teacher/          # Teacher routes (role-based)
│   │   │   ├── +layout.svelte # Teacher sidebar layout
│   │   │   ├── dashboard/
│   │   │   │   └── +page.svelte
│   │   │   ├── verification/ # (to be implemented)
│   │   │   ├── post-class/   # (to be implemented)
│   │   │   ├── schedule/     # (to be implemented)
│   │   │   ├── messages/     # (to be implemented)
│   │   │   └── earnings/     # (to be implemented)
│   │   ├── admin/            # Admin routes (role-based)
│   │   │   ├── +layout.svelte # Admin sidebar layout (dark theme)
│   │   │   ├── dashboard/
│   │   │   │   └── +page.svelte
│   │   │   └── verifications/ # (to be implemented)
│   │   ├── find-tutors/      # Public tutor search
│   │   │   └── +page.svelte
│   │   ├── streams/          # A/L streams information
│   │   │   └── +page.svelte
│   │   ├── career-guidance/  # Career guidance page
│   │   │   └── +page.svelte
│   │   └── tutor/            # Tutor profile pages (to be implemented)
│   │       └── [id]/
│   │           └── +page.svelte
│   └── static/               # Static assets served at root
├── package.json              # Dependencies and scripts
├── svelte.config.js          # SvelteKit configuration
├── tailwind.config.ts        # Tailwind CSS configuration
├── vite.config.ts            # Vite configuration
└── tsconfig.json             # TypeScript configuration
```

## Folder Usage

### `src/lib/`
Shared library code used across the application:
- **api/**: API client wrapper and endpoint-specific modules
- **components/**: Reusable Svelte components (UI primitives, layout components, domain-specific components)
- **stores/**: Svelte 5 rune stores for global state (auth, websocket, notifications)
- **schemas/**: Zod validation schemas mirroring backend Pydantic models
- **types/**: Shared TypeScript type definitions
- **utils/**: Helper functions (date formatting, currency formatting, etc.)

### `src/routes/`
SvelteKit file-based routing:
- **Root routes** (`+layout.svelte`, `+page.svelte`): Public pages accessible to all users
- **auth/**: Login and registration pages
- **student/**: Protected routes requiring student role, with sidebar layout
- **teacher/**: Protected routes requiring teacher role, with sidebar layout
- **admin/**: Protected routes requiring admin role, with dark sidebar layout
- **find-tutors/**: Public tutor search and filtering
- **streams/**: Information about A/L streams and subjects
- **career-guidance/**: Career guidance and AI chat teaser

## Getting Started

### Prerequisites
- Node.js 18+ 
- npm or yarn

### Installation

```bash
cd frontend
npm install
```

### Development

Start the development server:

```bash
npm run dev
```

The application will be available at `http://localhost:5173`

### Building for Production

```bash
npm run build
```

### Preview Production Build

```bash
npm run preview
```

## Development Notes

### Role-Based Access
- Route groups (`student/`, `teacher/`, `admin/`) enforce role-based access
- Login page redirects users to their appropriate dashboard based on selected role
- Layout files include role-specific sidebars and navigation

### Styling
- Custom CSS variables defined in `layout.css` for consistent theming
- Tailwind CSS utility classes for rapid development
- Design tokens: primary color (blue), accent color (saffron), muted colors, border colors

### State Management
- Svelte 5 runes (`$state`, `$derived`, `$effect`) for reactive state
- Auth store manages current user session and role
- Additional stores planned for websocket connections and notifications

### API Integration
- Base API client in `src/lib/api/client.ts` handles authentication headers
- Endpoint-specific modules to be added as backend is developed
- TanStack Svelte Query for data fetching and caching (to be integrated)

## Current Status

**Completed:**
- ✅ Project structure setup
- ✅ Tailwind CSS configuration with custom design tokens
- ✅ Public pages (index, find-tutors, streams, career-guidance)
- ✅ Authentication pages (login, register) with role selection
- ✅ Student dashboard with sidebar layout
- ✅ Teacher dashboard with sidebar layout
- ✅ Admin dashboard with dark sidebar layout
- ✅ Role-based routing and redirection
- ✅ API client base implementation
- ✅ Auth store implementation

**In Progress:**
- 🔄 Teacher verification flow
- 🔄 Booking system integration
- 🔄 Real-time messaging
- 🔄 AI career chat

**Pending:**
- ⏳ Component library (shadcn-svelte integration)
- ⏳ Zod validation schemas
- ⏳ Svelte Query integration
- ⏳ Backend API integration

## License

© 2026 EduLink Sri Lanka. All rights reserved.
