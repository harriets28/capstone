# Wanderlust — Travel Blog

A full-stack travel blog built with Django and PostgreSQL. Readers can browse travel stories by destination, like posts, save destinations to a travel wishlist, and leave comments. Content is managed by staff/admin users via Django's admin panel.

**Live site:** [https://wanderlust-travel-blog-96a6eae44782.herokuapp.com](https://wanderlust-travel-blog-96a6eae44782.herokuapp.com)  
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

Wanderlust is a magazine-style travel journal where staff writers publish destination stories. Visitors can browse all posts, filter by destination category, search by keyword, like their favourite stories, save destinations to a travel wishlist, and leave comments. Users must register and log in to interact.

### Target Audience

- Travel enthusiasts looking for destination inspiration
- Readers who enjoy long-form travel writing

### Project Goals

- Provide a clean, editorial reading experience on all devices
- Allow authenticated users to like, comment on, and wishlist stories
- Give staff full content control via the Django admin panel

---

## UX Design Process

### Strategy

The core value proposition is high-quality editorial travel content. The design intent was a premium magazine feel — not a generic blog. Key strategic decisions:

- **Editorial typography** over utilitarian fonts — Playfair Display for headings gives the feel of a print masthead
- **Warm parchment palette** (`#f7f3ee`) to evoke paper and reduce the clinical feel of a white background
- **Terracotta accent** (`#c4603a`) as the action colour — warm and travel-evocative without being generic
- **Authenticated interaction** — browsing is open to all, but liking, commenting, and wishlisting require login, which encourages registration without blocking content

### Scope — User Stories

| As a…           | I want to…                               | So that…                                    |
| --------------- | ---------------------------------------- | ------------------------------------------- |
| Visitor         | Browse all published travel stories      | I can find destinations that interest me    |
| Visitor         | Search and filter stories by destination | I can quickly find relevant content         |
| Visitor         | Read a full story                        | I can enjoy the content                     |
| Visitor         | Register for an account                  | I can interact with content                 |
| Registered user | Like/favourite stories                   | I can save posts I enjoy                    |
| Registered user | Add stories to my travel wishlist        | I can keep track of destinations to visit   |
| Registered user | Leave comments on stories                | I can join the conversation                 |
| Registered user | Reply to comments                        | I can respond to other users                |
| Registered user | Edit or delete my own comments           | I can manage my contributions               |
| Registered user | View and edit my profile                 | I can personalise my account                |
| Registered user | Upload a profile avatar                  | I can personalise how I appear to others    |
| Registered user | Delete my account                        | I can remove my data from the site          |
| Registered user | Submit a story pitch                     | I can contribute to the community           |
| Admin/staff     | Create, edit, and delete posts           | I can manage site content                   |
| Admin/staff     | Mark posts as featured                   | I can highlight top stories on the homepage |
| Admin/staff     | Approve or remove comments               | I can moderate the community                |
| Admin/staff     | Review story submissions                 | I can manage incoming contributor pitches   |

### Structure

The site is organised into clearly separated areas:

- **Homepage** — parallax hero + featured strip + recent stories grid
- **All Stories** — searchable, filterable, paginated post index
- **Post Detail** — full article + image carousel + comments + like + wishlist buttons
- **Category** — filtered post index per destination region
- **Profile** — user info, avatar, liked stories, wishlist, and comment history
- **Community** — grid of all active contributors
- **Submit a Story** — public pitch submission form
- **About** — editorial about page
- **Auth pages** — register, login, password reset flow

### Skeleton — Wireframes

Text wireframes were used in the planning phase to define layout hierarchy before visual styling.

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
│  Cover image / image carousel            │
│                                          │
│  Post content body (prose)               │
│                                          │
│  [❤️ Like]  [🗺️ Wishlist]  [🔗 Share]   │
│                                          │
│  Author card                             │
├──────────────────────────────────────────┤
│  Comments + replies + comment form       │
├──────────────────────────────────────────┤
│  Related posts                           │
└──────────────────────────────────────────┘

Profile
┌──────────────────────────────────────────┐
│  Full-screen hero with avatar, bio,      │
│  stats (liked / wishlist / comments)     │
│  [Edit Profile]  [Delete Account]        │
├──────────────────────────────────────────┤
│  Liked Stories grid                      │
│  Travel Wishlist grid                    │
│  Comment History list                    │
└──────────────────────────────────────────┘

Community
┌──────────────────────────────────────────┐
│  [card] [card] [card]                    │
│  avatar, name, location, bio, post count │
└──────────────────────────────────────────┘
```

### Surface

| Element      | Choice                   | Rationale                                              |
| ------------ | ------------------------ | ------------------------------------------------------ |
| Primary font | Playfair Display         | Classic editorial serif — evokes a print magazine      |
| Body font    | Source Serif 4           | Readable serif optimised for long-form reading         |
| UI font      | DM Sans                  | Clean sans-serif for navigation, labels, and metadata  |
| Background   | #f7f3ee (warm parchment) | Evokes paper; easier on the eyes than stark white      |
| Accent       | #c4603a (terracotta)     | Warm, travel-evocative; used for CTAs and hover states |
| Dark         | #1a1612 (near-black ink) | Richer than pure black; matches the warm palette       |

### Design Changes During Development

The following changes were made during development based on testing and evolving requirements. Each change is documented with the rationale.

| Original plan                      | Change made                                        | Reason                                                                              |
| ---------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Static hero image                  | Parallax scrolling hero                            | More engaging; sets the editorial tone on first impression                          |
| No category navigation on homepage | Category pills added below hero                    | Users needed a faster path to filtered content without going to the post list       |
| Standard Django messages framework | Floating toast notifications                       | Default messages disrupted page layout; toasts are less intrusive and auto-dismiss  |
| Single cover image per post        | Bootstrap carousel supporting up to 3 images       | Writers wanted to show multiple photos; carousel keeps the layout clean             |
| Basic profile page                 | Full-screen hero profile with centred stats layout | Profile needed to feel like a destination page, not a settings page                 |
| No community feature               | Community page added                               | Profiles existed but were undiscoverable; the community page creates a social layer |
| No contributor submissions         | Story submission form added                        | Opened a path for non-staff contributors without giving admin access                |
| No pagination                      | Paginator added to post list (9 per page)          | Performance and UX degraded with a large number of posts loading at once            |
| Full page reload on like           | AJAX like toggle                                   | Reloading the page on like felt jarring; AJAX keeps the user in context             |
| Like only                          | Wishlist toggle added                              | Users wanted a way to save posts they hadn't visited yet, separate from liking      |

---

## Features

### Implemented Features

- **Parallax hero** — full screen branded hero with scroll effect on homepage, all stories, and about pages
- **Featured post strip** — dark editorial strip showcasing randomly selected featured stories
- **Category filtering** — browse posts by destination region via pill navigation
- **Keyword search** — search across title, destination, and excerpt
- **Pagination** — paginated post list (9 posts per page)
- **Post detail** — full article with view count, author card, and related posts
- **Image carousel** — posts support up to three cover images in a Bootstrap carousel
- **AJAX like/unlike** — toggle likes without page reload; count updates in byline and button simultaneously
- **AJAX wishlist toggle** — save/remove posts from travel wishlist without page reload
- **Share button** — copies post URL to clipboard with visual confirmation
- **Threaded comments** — authenticated users can post, edit, delete, and reply to comments
- **User registration** — with duplicate email validation
- **User profiles** — avatar, bio, location, favourite destination, Instagram handle, liked stories, wishlist, and comment history
- **Avatar upload** — profile images cropped and stored via Cloudinary with face-gravity transformation
- **Community page** — grid of all users who have published at least one story
- **Story submission** — public form for contributor pitches with optional photo upload via Cloudinary
- **Account deletion** — users can permanently delete their account via a confirmation modal
- **Password reset** — full email-based password reset flow
- **Role-based access** — only staff can create posts via admin; all write actions require login
- **Flash messages** — floating toast notifications, auto-dismissed after 5 seconds
- **CKEditor** — rich text editor for post content in the admin panel
- **Fully responsive** — mobile navigation, fluid grid, breakpoints at 600px, 768px, and 900px
- **Custom 500 error page** — branded server error page

### Future Features

- Social sharing buttons (Twitter/X, Facebook)
- Map integration showing destinations
- Newsletter subscription
- User-submitted posts (currently staff-only via admin)

---

## Data Models

### Entity Relationship Diagram

```
User (Django built-in)
│
├── UserProfile (OneToOne)
│     bio, location, favourite_destination, instagram, avatar
│
├── Post (ForeignKey → author)
│     title, slug, destination, excerpt, content
│     status (draft/published), featured, view_count
│     cover_image, cover_image_2, cover_image_3
│     category (ForeignKey → Category)
│
├── Comment (ForeignKey → author + post)
│     body, approved, created_at
│     parent (self-referential ForeignKey for replies)
│
├── Like (ForeignKey → user + post)
│     unique_together constraint
│
└── Wishlist (ForeignKey → user + post)
      unique_together constraint

Category
  name, slug

StorySubmission
  name, email, destination, pitch, photo_url, photo, reviewed
```

### Custom Models

| Model           | Purpose                                                                       |
| --------------- | ----------------------------------------------------------------------------- |
| Post            | Core travel blog post with destination, status, featured flag, and view count |
| Category        | Destination grouping with auto-generated slug                                 |
| Comment         | User comment with approval flag and self-referential parent for replies       |
| Like            | One like per user/post enforced by unique_together                            |
| Wishlist        | One wishlist entry per user/post enforced by unique_together                  |
| UserProfile     | Extended user data including avatar, auto-created via Django signal           |
| StorySubmission | Public contributor pitch with optional photo, tracked via reviewed flag       |

---

## Technologies Used

**Backend**

- Python 3.12
- Django 4.2.11
- PostgreSQL (production) / SQLite (development)
- dj-database-url
- django-ckeditor 6.7.3 (rich text editor for admin)
- Pillow 12.1.1 (image handling)
- python-dotenv (environment variable management)

**Media & File Storage**

- Cloudinary (avatar and story submission photo storage with image transformations)
- django-cloudinary-storage

**Frontend**

- Bootstrap 5.3
- Bootstrap Icons
- Google Fonts — Playfair Display, Source Serif 4, DM Sans
- Vanilla JavaScript (AJAX like/wishlist toggles, parallax, mobile nav, clipboard share, toast auto-dismiss)

**Deployment**

- Heroku
- Gunicorn
- WhiteNoise (static files)
- Git / GitHub

---

## Testing

### Testing Approach

Testing was carried out at three levels: automated Python unit tests covering models, views, and forms; manual JavaScript testing of all client-side interactive features; and manual end-to-end testing across browsers and devices.

---

### Python Automated Tests

Tests are located in `blog/tests.py` and can be run with:

```bash
python manage.py test
```

**Result: 10 tests, 0 failures**

#### Test Cases

| Test Class            | Test Method                        | What is tested                                  | Expected outcome              | Actual result |
| --------------------- | ---------------------------------- | ----------------------------------------------- | ----------------------------- | ------------- |
| CategoryModelTest     | test_slug_auto_generated           | Slug generated from name on save                | slug == 'asia'                | ✅ Pass       |
| CategoryModelTest     | test_str_representation            | `__str__` returns category name                 | str == 'Asia'                 | ✅ Pass       |
| PostModelTest         | test_slug_auto_generated           | Slug generated from title on save               | slug == 'sunset-in-santorini' | ✅ Pass       |
| PostModelTest         | test_str_representation            | `__str__` returns post title                    | str == 'Sunset in Santorini'  | ✅ Pass       |
| PostModelTest         | test_like_count_zero_by_default    | New post has zero likes                         | like_count == 0               | ✅ Pass       |
| PostModelTest         | test_comment_count_zero_by_default | New post has zero approved comments             | comment_count == 0            | ✅ Pass       |
| PostModelTest         | test_is_liked_by_unauthenticated   | Anonymous user cannot like                      | is_liked_by == False          | ✅ Pass       |
| LikeModelTest         | test_like_created                  | Like increments like_count and is_liked_by      | like_count == 1, True         | ✅ Pass       |
| LikeModelTest         | test_like_unique_per_user_and_post | Duplicate like raises IntegrityError            | IntegrityError raised         | ✅ Pass       |
| UserProfileSignalTest | test_profile_created_on_user_save  | UserProfile auto-created when User is saved     | user.profile exists           | ✅ Pass       |
| HomeViewTest          | test_home_200                      | Homepage returns 200                            | status_code == 200            | ✅ Pass       |
| HomeViewTest          | test_correct_template              | Homepage uses correct template                  | blog/home.html used           | ✅ Pass       |
| HomeViewTest          | test_published_only                | Only published posts appear in context          | draft excluded                | ✅ Pass       |
| PostDetailViewTest    | test_published_post_200            | Published post detail returns 200               | status_code == 200            | ✅ Pass       |
| PostDetailViewTest    | test_draft_post_404                | Draft post detail returns 404                   | status_code == 404            | ✅ Pass       |
| PostDetailViewTest    | test_comment_posting               | Authenticated POST creates comment              | comment saved to DB           | ✅ Pass       |
| ToggleLikeViewTest    | test_redirect_when_logged_out      | Unauthenticated like request redirects to login | redirect to login             | ✅ Pass       |
| ToggleLikeViewTest    | test_like                          | Authenticated like creates Like object          | Like exists in DB             | ✅ Pass       |
| ToggleLikeViewTest    | test_unlike                        | Second like request removes Like object         | Like removed from DB          | ✅ Pass       |
| PostListSearchTest    | test_keyword_search                | Search query filters posts by title/destination | matching posts returned       | ✅ Pass       |
| PostListSearchTest    | test_category_filter               | Category param filters posts by category        | correct posts returned        | ✅ Pass       |
| CommentFormTest       | test_valid_comment                 | Valid body passes form validation               | form.is_valid() == True       | ✅ Pass       |
| CommentFormTest       | test_empty_comment                 | Empty body fails validation                     | form.is_valid() == False      | ✅ Pass       |
| CommentFormTest       | test_too_short_comment             | Body under 3 chars fails validation             | form.is_valid() == False      | ✅ Pass       |
| AccessControlTest     | test_edit_profile_redirect         | Edit profile redirects unauthenticated user     | redirect to /accounts/login/  | ✅ Pass       |

---

### JavaScript Testing

JavaScript is used for the following interactive features. All were tested manually in Chrome and Safari.

#### Test Cases

| Feature                       | Test                              | Expected outcome                                                             | Actual result |
| ----------------------------- | --------------------------------- | ---------------------------------------------------------------------------- | ------------- |
| AJAX like toggle              | Click like button while logged in | Like count increments; button style changes to liked state                   | ✅ Pass       |
| AJAX unlike toggle            | Click like button again           | Like count decrements; button returns to default style                       | ✅ Pass       |
| Like count in byline          | Toggle like                       | Byline like count updates in sync with button count                          | ✅ Pass       |
| AJAX wishlist toggle — add    | Click wishlist button             | Button text changes to "Saved to Wishlist"; button highlighted               | ✅ Pass       |
| AJAX wishlist toggle — remove | Click wishlist button again       | Button text returns to "Add to Wishlist"; highlighting removed               | ✅ Pass       |
| Share button                  | Click share                       | URL copied to clipboard; button text changes to "Link copied!" for 2 seconds | ✅ Pass       |
| Parallax hero                 | Scroll page                       | Background image moves at a different rate to the page content               | ✅ Pass       |
| Nav scroll behaviour          | Scroll past 50px                  | Nav background transitions from transparent to frosted white                 | ✅ Pass       |
| Nav white text on hero        | Load page at top                  | Nav links appear white against the dark hero image                           | ✅ Pass       |
| Mobile menu toggle            | Click Menu button on mobile       | Nav links expand; button label changes to "Close"                            | ✅ Pass       |
| Mobile menu close             | Click Close button                | Nav links collapse; button label returns to "Menu"                           | ✅ Pass       |
| Toast auto-dismiss            | Trigger a flash message           | Toast fades out and is removed from DOM after 5 seconds                      | ✅ Pass       |
| Comment edit toggle           | Click Edit on own comment         | Inline edit form appears; comment text becomes editable                      | ✅ Pass       |
| Comment edit cancel           | Click Cancel in edit form         | Edit form hides; original comment text restored                              | ✅ Pass       |
| Reply form toggle             | Click Reply on any comment        | Reply form appears below the comment                                         | ✅ Pass       |
| Reply form cancel             | Click Cancel in reply form        | Reply form hides                                                             | ✅ Pass       |

---

### Manual End-to-End Testing

| Feature                 | Steps                                   | Expected outcome                                         | Actual result |
| ----------------------- | --------------------------------------- | -------------------------------------------------------- | ------------- |
| Homepage loads          | Navigate to /                           | Page loads with hero, featured strip, and recent stories | ✅ Pass       |
| Search                  | Enter keyword in search box             | Matching posts displayed; non-matching excluded          | ✅ Pass       |
| Pagination              | Navigate to next/previous page          | Correct posts shown per page; page number highlighted    | ✅ Pass       |
| Category filter         | Click a category pill                   | Only posts in that category shown                        | ✅ Pass       |
| Register                | Submit valid registration form          | Account created; logged in; redirected to homepage       | ✅ Pass       |
| Duplicate email         | Submit registration with existing email | Form error shown; account not created                    | ✅ Pass       |
| Login / logout          | Sign in and out                         | Session created/destroyed correctly                      | ✅ Pass       |
| Password reset          | Request reset link; set new password    | Email sent (console in dev); new password accepted       | ✅ Pass       |
| Unauthenticated comment | POST comment while logged out           | Redirected to login page                                 | ✅ Pass       |
| Post comment            | Submit comment while logged in          | Comment appears on page                                  | ✅ Pass       |
| Edit comment            | Click edit, change text, save           | Updated text displayed                                   | ✅ Pass       |
| Delete comment          | Click delete, confirm                   | Comment removed from page                                | ✅ Pass       |
| Post reply              | Submit reply form                       | Reply nested under parent comment                        | ✅ Pass       |
| Image carousel          | View post with multiple images          | Carousel navigates between images correctly              | ✅ Pass       |
| Upload avatar           | Submit edit profile with image          | Avatar displayed on profile page                         | ✅ Pass       |
| Edit profile            | Update bio, location, etc.              | Changes saved and displayed on profile                   | ✅ Pass       |
| Delete account          | Open modal, confirm deletion            | Account deleted; redirected to homepage; session ended   | ✅ Pass       |
| Wishlist on profile     | Add posts to wishlist; view profile     | Wishlisted posts appear in profile wishlist section      | ✅ Pass       |
| Community page          | Navigate to /community/                 | All active contributors shown with stats                 | ✅ Pass       |
| Story submission        | Submit pitch form                       | Success message shown; submission saved in admin         | ✅ Pass       |
| Admin post CRUD         | Create, edit, delete post in admin      | Changes reflected on site                                | ✅ Pass       |
| Admin submission review | Mark submission as reviewed             | Reviewed field updates in admin list                     | ✅ Pass       |
| View count              | Visit post detail page                  | View count increments on each visit                      | ✅ Pass       |
| Related posts           | View post with a category               | Up to 3 posts from same category shown at bottom         | ✅ Pass       |
| Custom 500 page         | Trigger server error                    | Branded 500 page displayed                               | ✅ Pass       |

### Responsiveness Testing

Tested on: Chrome (Mac), Safari (Mac), Chrome Mobile (Android), Safari Mobile (iOS).  
Breakpoints tested: 390px, 768px, 1024px, 1440px.

| Breakpoint | Feature checked                  | Result  |
| ---------- | -------------------------------- | ------- |
| 390px      | Single column stories grid       | ✅ Pass |
| 390px      | Mobile nav menu                  | ✅ Pass |
| 390px      | Category bar horizontal scroll   | ✅ Pass |
| 768px      | Two column stories grid          | ✅ Pass |
| 768px      | Featured strip stacks vertically | ✅ Pass |
| 1024px+    | Three column stories grid        | ✅ Pass |

### Validator Testing

- HTML — validated via [W3C Markup Validator](https://validator.w3.org/)
- CSS — validated via [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- Python — PEP8 compliance checked via `pycodestyle`

---

## Deployment

### Prerequisites

- Python 3.12
- A [Cloudinary](https://cloudinary.com/) account (free tier is sufficient)
- A [Heroku](https://heroku.com/) account for production deployment

### Local Development

```bash
# 1. Clone the repo
git clone https://github.com/harriets28/capstone.git
cd capstone

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file and add your values
cp .env.example .env
```

Your `.env` file should contain:

```
SECRET_KEY=your-django-secret-key
DEBUG=True
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

```bash
# 5. Apply migrations
python manage.py migrate

# 6. Create a superuser (for admin access)
python manage.py createsuperuser

# 7. Collect static files (if needed)
python manage.py collectstatic

# 8. Run the development server
python manage.py runserver
```

The site will be available at `http://127.0.0.1:8000/`.

Admin panel is at `http://127.0.0.1:8000/admin/` — log in with your superuser credentials to create categories and posts.

### Heroku Deployment

```bash
# 1. Log in to Heroku
heroku login

# 2. Create a new Heroku app
heroku create your-app-name

# 3. Add the PostgreSQL add-on
heroku addons:create heroku-postgresql:essential-0

# 4. Set all required environment variables
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG='False'
heroku config:set CLOUDINARY_CLOUD_NAME='your-cloud-name'
heroku config:set CLOUDINARY_API_KEY='your-api-key'
heroku config:set CLOUDINARY_API_SECRET='your-api-secret'
heroku config:set EMAIL_HOST_USER='your-email@gmail.com'
heroku config:set EMAIL_HOST_PASSWORD='your-gmail-app-password'

# 5. Push to Heroku
git push heroku main

# 6. Run database migrations
heroku run python manage.py migrate

# 7. Create a superuser on the production database
heroku run python manage.py createsuperuser
```

### Required Files for Deployment

| File               | Purpose                                                                     |
| ------------------ | --------------------------------------------------------------------------- |
| `Procfile`         | Tells Heroku to run the app with Gunicorn (`web: gunicorn wanderlust.wsgi`) |
| `requirements.txt` | Lists all Python dependencies                                               |
| `runtime.txt`      | Specifies the Python version                                                |
| `.env`             | Local environment variables (not committed to Git)                          |

### Environment Variables

| Variable              | Description                                          |
| --------------------- | ---------------------------------------------------- |
| SECRET_KEY            | Django secret key — must be kept private             |
| DEBUG                 | Set to `False` in production                         |
| DATABASE_URL          | PostgreSQL connection string — auto-set by Heroku    |
| CLOUDINARY_CLOUD_NAME | Your Cloudinary cloud name                           |
| CLOUDINARY_API_KEY    | Your Cloudinary API key                              |
| CLOUDINARY_API_SECRET | Your Cloudinary API secret                           |
| EMAIL_HOST_USER       | Gmail address used to send password reset emails     |
| EMAIL_HOST_PASSWORD   | Gmail app password (not your regular Gmail password) |

### Security Measures

- `SECRET_KEY` stored as environment variable — never committed to Git
- `DEBUG=False` in production prevents detailed error pages being shown to users
- `.env` file excluded via `.gitignore`
- CSRF protection enabled on all forms via Django's built-in middleware
- `@login_required` decorator applied to all write operations (like, wishlist, comment, edit profile, delete account)
- Cloudinary credentials stored as environment variables

---

## AI Reflections

### 8.1 — AI Used to Assist in Code Creation

AI was used to scaffold boilerplate sections of the project — initial model skeletons, URL pattern structures, and form class outlines. The core architectural decisions were made manually: the data model relationships (including the self-referential `parent` field on `Comment` for threaded replies, and the `unique_together` constraint on both `Like` and `Wishlist`), the signal pattern for auto-creating `UserProfile` on registration, and the AJAX implementation for like and wishlist toggling. AI-generated code was always reviewed, tested, and adapted before use rather than accepted as-is.

### 8.2 — AI Used to Assist in Debugging

Most AI involvement in this project was in diagnosing bugs found during development and manual testing.

**Bootstrap carousel cropping images** — During testing, cover images in the post detail carousel were being cut off at an inconsistent height. AI suggested opening browser dev tools and inspecting the computed height of each carousel element. The issue was that `.carousel`, `.carousel-inner`, and `.carousel-item` were inheriting different heights from Bootstrap defaults. AI suggested explicitly setting a unified height across all three selectors in CSS, which resolved the cropping.

**Horizontal scroll not working on mobile** — The category pill bar on the post list page failed to scroll horizontally on touch devices. AI identified that `overflow-x: auto` alone was not sufficient for mobile — `scrollbar-width: none` and `-webkit-scrollbar { display: none }` were also needed to enable smooth touch scrolling while hiding the scrollbar. AI also flagged that flex child elements needed `white-space: nowrap` to prevent the pills from wrapping onto a second line.

**Missing UserProfile for pre-existing users** — After the `post_save` signal was added to auto-create a `UserProfile`, users created before the signal was in place had no profile, causing `RelatedObjectDoesNotExist` errors on the profile page. AI explained that `post_save` signals only fire on new object creation and suggested creating profiles for existing users via a one-off script in the Django shell.

**URL ordering conflict** — The `profile/edit/` path was being caught by the `profile/<str:username>/` pattern, resulting in Django looking for a user with username `edit`. AI explained Django's top-down URL matching behaviour and confirmed that `profile/edit/` needed to be defined above the dynamic `<str:username>` pattern in `urls.py`.

### 8.3 — AI Used to Optimise for Performance and UX

AI recommended two specific optimisations during development. First, switching the like button from a standard form POST (full page reload) to an AJAX `fetch` call — this removed a jarring page refresh on every like interaction. The same pattern was later applied to the wishlist toggle. Second, AI identified that the `profile_view` queryset was making unnecessary database hits and recommended adding `select_related('post')` to the liked posts and wishlist querysets to reduce queries.

### 8.4 — AI Used to Create Automated Unit Tests

AI was used to generate the initial set of unit tests in `blog/tests.py`. The generated tests covered model `__str__` methods, slug auto-generation, like/comment counts, and basic view responses. Adjustments were required after generation: the `AccessControlTest` redirect URL needed to be updated to match the project's `LOGIN_URL = '/accounts/login/'` setting, and some test setup methods needed additional fixtures (e.g. a `Category` instance) to match the actual model constraints. The final test suite runs 10 tests with 0 failures.

### 8.4 — Reflection on AI's Role in the Overall Workflow

AI contributed meaningfully at two distinct stages of the workflow. The first was feature development — describing a desired outcome in plain terms and having AI generate a working implementation to build from. This was particularly useful for features with several moving parts, such as the AJAX wishlist toggle (requiring a Django view, a JSON response, and coordinated frontend JS), the threaded comment reply system (self-referential model, nested template loop, and toggle behaviour), and the Cloudinary avatar upload with face-gravity cropping. In each case, the approach was to describe the intended behaviour, review the generated code against the project's existing patterns, and adapt it before integrating.

The second was as a diagnostic tool — interpreting browser dev tools output to pinpoint CSS rendering bugs, explaining Django's URL resolution order when a routing conflict appeared, and generating a first draft of test cases that could be refined rather than written from scratch. The development process remained developer-led throughout — AI was used to accelerate implementation and unblock problems, but decisions about what to build, how the data should be modelled, and whether generated code was fit for purpose were always made by the developer.
