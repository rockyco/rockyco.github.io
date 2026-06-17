source "https://rubygems.org"

# Local preview only. GitHub Pages builds with its own toolchain
# (.github/workflows/jekyll-gh-pages.yml), so this file is gitignored from the build.
gem "jekyll", "~> 4.3"
gem "minima"
# Use the C-based SCSS converter (matches GitHub Pages; avoids the dart-sass
# musl issue in the Alpine build container).
gem "jekyll-sass-converter", "~> 2.0"

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-sitemap"
end
