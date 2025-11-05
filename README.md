# static-site-generator
Part of the ![Boot.Dev curriculum](https://www.boot.dev?bannerlord=shout64), this generator converts markdown files into HTML, and puts them (and your media) into a public directory to serve out as a static site.

## Installation and Use
- Fork and clone the repo to your local machine.
- Update your CSS and add any images/media to the Static folder.
- Under the Content folder add your Markdown files and site navigation structure for your custom site.
- If you want to test locally:
  - Update src/main.py to use "public" instead of "docs" in the "main()" function.
  <img width="468" height="86" alt="image" src="https://github.com/user-attachments/assets/5c7309e9-d591-49a7-aefd-2a61574730f4" />

  - Run main.sh to generate your site and run your site locally. Visit http://localhost:8888 to see your site running locally.
- To push to production and make a live site (with GitHub Pages):
  - If changed, set the main function calls in src/main.py back to "docs" (see previous step for testing locally).
  - Update build.sh and replace my repo name with your own repo's name
  - Run build.sh to generate your site with the proper navigation for your repo.
  - Commit and push your changes to GitHub.
  - In your repo on GitHub, navigate to Settings > Pages
    - Set Source to "Deploy from a branch".
    - Set your branch to "main" (or whatever your main branch is) and set folder to "/docs" and click Save.
  - You should now be able to see your website live at https://YOUR-USERNAME.github.io/YOUR-REPO/ (there should be a link at the top of the screen.
  - To make changes to your site, just update your files in the Content folder, run build.sh and push your changes up to your repo.
 
## Demo
You can see the demo of the site used in the Boot.Dev course here: ![Demo Website](https://shout64.github.io/static-site-generator/)
