# rockyco.github.io

Personal academic website for Jie Lei, Research Fellow at the University of Technology Sydney.
Built with Jekyll and deployed on GitHub Pages.

Live site: https://rockyco.github.io

## Structure

```
_config.yml          Jekyll configuration and nav
index.md             Home
about.md             Bio, experience, education
work.md              Qualitative showcase of FPGA design work
publications.md      Google Scholar pointer
blog.md              Blog index
_posts/              Blog posts (English + Chinese, paired by translation_id)
_layouts/ _includes/ _sass/ assets/css/   Custom theme (Fraunces + Newsreader)
.github/workflows/jekyll-gh-pages.yml      Build and deploy
```

## Local development

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000
```

Content and design are maintained with the `rockyco-website` skill, which sources design
descriptions from the Python2Verilog repository and keeps blog posts mirrored in English and
Chinese.

## License

MIT. See [LICENSE](LICENSE).
