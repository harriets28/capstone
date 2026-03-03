# Wanderlust — Travel Blog

A full-stack travel blog built with Django and PostgreSQL. Readers can browse travel stories by destination, like posts, and leave comments. Content is managed by staff/admin users via Django's admin panel.

**GitHub:** [https://github.com/harriets28/capstone](https://github.com/harriets28/capstone)

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [UX Design Process](#ux-design-process)
3. [Features](#features)
4. [Data Models](#data-models)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [AI Reflections](#ai-reflections)

---

## Project Overview

Wanderlust is a magazine-style travel journal where staff writers publish destination stories. Visitors can browse all posts, filter by destination category, search by keyword, like their favourite stories, and leave comments. Users must register and log in to interact.

### Target Audience

- Travel enthusiasts looking for destination inspiration
- Readers who enjoy long-form travel writing

### Project Goals

- Provide a clean, editorial reading experience on all devices
- Allow authenticated users to like and comment on stories
- Give staff full content control via the Django admin panel

---

## UX Design Process

### Strategy

The core value proposition is high-quality editorial travel content. The design takes a magazine/editorial approach — generous typography, a parallax hero, and a warm parchment colour palette — to evoke the feel of a premium travel magazine.

### Scope — User Stories

| As a…           | I want to…                               | So that…                                    |
| --------------- | ---------------------------------------- | ------------------------------------------- |
| Visitor         | Browse all published travel stories      | I can find destinations that interest me    |
| Visitor         | Search and filter stories by destination | I can quickly find relevant content         |
| Visitor         | Read a full story                        | I can enjoy the content                     |
| Visitor         | Register for an account                  | I can interact with content                 |
| Registered user | Like/favourite stories                   | I can save posts I enjoy                    |
| Registered user | Leave comments on stories                | I can join the conversation                 |
| Registered user | Delete my own comments                   | I can manage my contributions               |
| Registered user | View and edit my profile                 | I can personalise my account                |
| Admin/staff     | Create, edit, and delete posts           | I can manage site content                   |
| Admin/staff     | Mark posts as featured                   | I can highlight top stories on the homepage |
| Admin/staff     | Approve or remove comments               | I can moderate the community                |

### Structure

- **Homepage** — parallax hero + featured strip + recent stories grid
- **All Stories** — searchable, filterable post index
- **Post Detail** — full article + comments + like button
- **Category** — filtered post index per destination region
- **Profile** — user info + liked stories
- **Auth pages** — register, login

### Skeleton — Wireframes

```
Homepage
┌──────────────────────────────────────────┐
│ NAV: Wanderlust ✦   Stories  Sign In  Join│
├──────────────────────────────────────────┤
│                                          │
│   PARALLAX HERO                          │
│   ✦ Wanderlust                           │
│   Stories from the edges of the world    │
│   [Explore Stories →]                    │
│                                          │
├──────────────────────────────────────────┤
│  Featured post 1  │  Featured post 2     │
├──────────────────────────────────────────┤
│ CATEGORY PILLS: All  Asia  Europe  Americas│
├──────────────────────────────────────────┤
│ Recent Stories ──────────────── View all │
│ [card]  [card]  [card]                   │
└──────────────────────────────────────────┘

Post Detail
┌──────────────────────────────────────────┐
│ NAV                                      │
├──────────────────────────────────────────┤
│  CATEGORY TAG                            │
│  H1 Post Title                           │
│  Excerpt (italic)                        │
│  By Author · Date · 📍 Destination       │
├──────────────────────────────────────────┤
│  Post content body (prose)               │
│                                          │
│  [❤️ Like button]                        │
│                                          │
│  Author card                             │
├──────────────────────────────────────────┤
│  Comments + comment form                 │
└──────────────────────────────────────────┘
```

### Surface

| Element      | Choice                   | Rationale                                  |
| ------------ | ------------------------ | ------------------------------------------ |
| Primary font | Playfair Display         | Classic editorial serif                    |
| Body font    | Source Serif 4           | Readable serif for long-form content       |
| UI font      | DM Sans                  | Clean sans-serif for navigation and labels |
| Background   | #f7f3ee (warm parchment) | Evokes paper, reduces eye strain           |
| Accent       | #c4603a (terracotta)     | Warm, travel-evocative colour              |

**Design changes during development:**

- Added parallax hero instead of a static image — more engaging on the homepage
- Category pills added below hero for quick filtering
- Flash messages changed to floating toast notifications for cleaner UX
- Featured strip added below hero to showcase more posts without scrolling

---

## Features

### Implemented Features

- **Parallax hero** — full screen branded hero with scroll effect
- **Featured post strip** — dark editorial strip showcasing featured stories
- **Category filtering** — browse posts by destination region
- **Keyword search** — search across title, destination and excerpt
- **Post detail** — full article with author card
- **AJAX like/unlike** — toggle likes without page reload
- **Comments** — authenticated users can post and delete their own comments
- **User registration** — with email validation
- **User profiles** — bio, location, website and liked stories
- **Role-based access** — only staff can create posts via admin
- **Flash messages** — toast notifications for user actions
- **Fully responsive** — works on mobile, tablet and desktop

### Future Features

- Pagination on post lists
- Social sharing buttons
- Map integration showing destinations
- Newsletter subscription

---

## Data Models

### Entity Relationship Diagram

```
User (Django built-in)
│
├── UserProfile (OneToOne)
│     bio, location, website
│
├── Post (ForeignKey → author)
│     title, slug, destination, excerpt, content
│     status (draft/published), featured
│     category (ForeignKey → Category)
│
├── Comment (ForeignKey → author + post)
│     body, approved, created_at
│
└── Like (ForeignKey → user + post)
      unique_together constraint

Category
  name, slug, description
```

### Custom Models

| Model       | Purpose                                                          |
| ----------- | ---------------------------------------------------------------- |
| Post        | Core travel blog post with destination, status and featured flag |
| Category    | Destination grouping with auto-generated slug                    |
| Comment     | User comment with approval flag                                  |
| Like        | One like per user/post enforced by unique_together               |
| UserProfile | Extended user data, auto-created via Django signal               |

---

## Technologies Used

**Backend**

- Python 3.12
- Django 4.2
- PostgreSQL (production) / SQLite (development)
- dj-database-url

**Frontend**

- Bootstrap 5.3
- Bootstrap Icons
- Google Fonts — Playfair Display, Source Serif 4, DM Sans
- Vanilla JavaScript (AJAX like toggle, parallax, mobile nav)

**Deployment**

- Heroku
- Gunicorn
- WhiteNoise (static files)
- Git / GitHub

---

## Testing

### Running the Tests

```bash
python manage.py test
```

Result: **10 tests, 0 failures**

### Test Coverage

| Test Class            | What it tests                                         |
| --------------------- | ----------------------------------------------------- |
| CategoryModelTest     | Slug auto-generation, **str**                         |
| PostModelTest         | Slug, **str**, like count, comment count, is_liked_by |
| LikeModelTest         | Like creation, unique constraint                      |
| UserProfileSignalTest | Auto-created profile on user registration             |
| HomeViewTest          | 200 response, correct template, published-only filter |
| PostDetailViewTest    | 200 for published, 404 for draft, comment posting     |
| ToggleLikeViewTest    | Redirect when logged out, like, unlike                |
| PostListSearchTest    | Keyword search, category filter                       |
| CommentFormTest       | Valid comment, empty comment, too short               |
| AccessControlTest     | Edit profile redirects when not logged in             |

### Manual Testing

| Feature                           | Test                    | Result  |
| --------------------------------- | ----------------------- | ------- |
| Homepage loads                    | Navigate to /           | ✅ Pass |
| Parallax scrolls                  | Scroll homepage         | ✅ Pass |
| Search works                      | Search ?q=Kyoto         | ✅ Pass |
| Category filter                   | Click category pill     | ✅ Pass |
| Register new user                 | Submit valid form       | ✅ Pass |
| Duplicate email rejected          | Submit existing email   | ✅ Pass |
| Login / logout                    | Sign in and out         | ✅ Pass |
| Unauthenticated comment redirects | POST when logged out    | ✅ Pass |
| Authenticated comment posts       | POST when logged in     | ✅ Pass |
| AJAX like toggle                  | Click like button       | ✅ Pass |
| AJAX unlike toggle                | Click like button again | ✅ Pass |
| Delete own comment                | Click delete            | ✅ Pass |
| Edit profile saves                | Submit edit form        | ✅ Pass |
| Admin post CRUD                   | Create/edit/delete post | ✅ Pass |
| Responsive on mobile              | iPhone 12 Pro viewport  | ✅ Pass |

### Responsiveness Testing

Tested on: Chrome (Mac), Safari (Mac), Chrome Mobile (Android), Safari Mobile (iOS).
Breakpoints tested: 390px, 768px, 1024px, 1440px.

---

## Deployment

### Local Development

```bash
# 1. Clone the repo
git clone https://github.com/harriets28/capstone.git
cd capstone

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cp .env.example .env
# Edit .env with your values

# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Run server
python manage.py runserver
```

### Heroku Deployment

```bash
# 1. Login to Heroku
heroku login

# 2. Create app
heroku create your-app-name

# 3. Add PostgreSQL
heroku addons:create heroku-postgresql:essential-0

# 4. Set environment variables
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG='False'

# 5. Push code
git push heroku main

# 6. Run migrations
heroku run python manage.py migrate

# 7. Create superuser
heroku run python manage.py createsuperuser
```

### Environment Variables

| Variable     | Description                   |
| ------------ | ----------------------------- |
| SECRET_KEY   | Django secret key             |
| DEBUG        | Set to False in production    |
| DATABASE_URL | Auto-set by Heroku PostgreSQL |

### Security

- SECRET_KEY stored as environment variable
- DEBUG=False in production
- .env excluded via .gitignore
- CSRF protection on all forms
- @login_required on all write operations

---

## AI Reflections

### Code Generation

AI was used to scaffold the initial project structure and boilerplate. Key decisions were made manually — the data model relationships, the slug auto-generation logic, and the signal pattern for auto-creating UserProfile on registration. AI suggestions were reviewed and adapted throughout.

### Debugging

AI tools helped identify two bugs: a missing UserProfile for users created before signals were added, and a URL ordering issue where `profile/edit/` was being matched by the `profile/<str:username>/` pattern. In both cases the AI correctly identified the root cause.

### Performance and UX

AI suggested switching the like button from a full page reload to an AJAX fetch call, which improved the perceived responsiveness. It also recommended using select_related() on querysets to reduce database queries.

### Automated Tests

AI was used to generate an initial set of test cases. These required adjustments — for example the redirect URL in the access control test needed to match the project's LOGIN_URL setting.

### Overall Impact

AI tools reduced time spent on repetitive boilerplate and accelerated debugging. The most valuable use was as a second-opinion tool for architectural decisions. Development remained developer-led throughout.
