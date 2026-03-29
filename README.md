# 🚀 My Portfolio

An interactive personal portfolio built with **[Reflex](https://reflex.dev/)**, a pure Python framework for building web applications. This portfolio belongs to **Mario C.**, Actuary and Software Developer focused on robust solutions, mathematical models, and automation.

> **Note**: This template is completely free to use! Feel free to fork it, modify it, and use it for your own portfolio. This project was heavily inspired by the design and vibe of [t3.gg](https://t3.gg/).

## ✨ Features

- Home, About, Projects, and Blog integrated.
- **Dynamic Blog**: Reads Markdown articles directly from the `blog_posts/` folder.
- **Centralized Data**: All personal information and projects are easily managed via `content.json`.
- **Modern Styling**: Uses TailwindCSS integrated through the Reflex V4 plugin.

## 🛠 Core Technologies

- **Python 3.13+**
- **Reflex** (`>=0.8.28`) for the complete creation of the UI and logic.
- **Python-Frontmatter** for managing metadata in blog posts (`.md`).
- **Tailwind V4 Plugin**.
- **[uv](https://docs.astral.sh/uv/)** for ultra-fast Python package and project management.

## 📁 Project Structure

```text
├── Mi_portafolio/          # Core logic of the Reflex framework.
│   ├── backend/            # Global state management or other backend services.
│   ├── components/         # Reusable UI components (layout, navbar, etc.)
│   └── pages/              # Reflex route modules (index, about, projects, blog, post)
├── blog_posts/             # Articles and posts in raw Markdown format.
├── content.json            # Lightweight database for bio, urls, and projects.
├── pyproject.toml          # Package manifest and system dependencies.
└── rxconfig.py             # Global Reflex configuration and plugins.
```

## 🚀 Installation and Usage

This project uses `uv` for dependency management.

1. **Clone the repository and enter the directory**:
   ```bash
   git clone <repo-url>
   cd Mi-portafolio
   ```

2. **Sync the project with `uv`**:
   This will automatically create a virtual environment and install the dependencies from `pyproject.toml`.
   ```bash
   uv sync
   ```

3. **Initialize and run in development mode**:
   ```bash
   uv run reflex init
   uv run reflex run
   ```
   Open [http://localhost:3000](http://localhost:3000) in your web browser.

## 📝 Content Management

- **Profile and Projects**: Edit the `content.json` file to modify personal data, biography, GitHub/LinkedIn links, and your projects carousel.
- **Blog Posts**: To add a new post, create an `.md` file in the `blog_posts/` folder using *frontmatter* blocks in the header (YAML) and your content below. Reflex will render it interactively at the `/blog/[slug]` route.

