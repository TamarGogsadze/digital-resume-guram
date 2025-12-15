# Deploy Your Digital Resume Dashboard Online - FREE

## Quick Deployment to Render (Recommended - 100% Free)

### Step 1: Prepare Your Files
Your files are already prepared! You need:
- ✅ app.py (updated for deployment)
- ✅ requirements.txt (includes gunicorn)
- ✅ Procfile (deployment configuration)
- ✅ assets/photo.jpg (your photo)

### Step 2: Create a GitHub Account (if you don't have one)
1. Go to https://github.com
2. Sign up for a free account

### Step 3: Create a New Repository
1. Log into GitHub
2. Click the "+" icon → "New repository"
3. Name it: `digital-resume`
4. Make it **Public**
5. DO NOT initialize with README
6. Click "Create repository"

### Step 4: Upload Your Files to GitHub

**Option A: Using GitHub Website (Easiest)**
1. In your new repository, click "uploading an existing file"
2. Drag and drop ALL these files:
   - app.py
   - requirements.txt
   - Procfile
   - Create a folder called "assets" and upload photo.jpg into it
3. Click "Commit changes"

**Option B: Using Git Command Line**
```bash
cd "C:\Users\TaGogsadze\Desktop\Digital Resume"
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR-USERNAME/digital-resume.git
git push -u origin main
```

### Step 5: Deploy to Render
1. Go to https://render.com
2. Sign up using your GitHub account
3. Click "New +" → "Web Service"
4. Click "Connect" next to your `digital-resume` repository
5. Configure:
   - **Name**: digital-resume (or any name you want)
   - **Region**: Choose closest to you
   - **Branch**: main
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:server`
   - **Plan**: **Free** (select this!)
6. Click "Create Web Service"
7. Wait 5-10 minutes for deployment

### Step 6: Access Your Live Website!
Once deployed, Render will give you a URL like:
`https://digital-resume-XXXX.onrender.com`

**That's your live resume dashboard! 🎉**

## Alternative Free Hosting Options

### Option 2: Railway.app
1. Go to https://railway.app
2. Sign in with GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Free tier: 500 hours/month

### Option 3: Fly.io
1. Go to https://fly.io
2. Sign up and install Fly CLI
3. Run: `fly launch` in your project folder
4. Free tier: 2,340 hours/month

## Important Notes

### Render Free Tier Limitations:
- ✅ Completely FREE forever
- ✅ Custom domain support
- ⚠️ App "sleeps" after 15 minutes of inactivity
- ⚠️ Takes 30-50 seconds to wake up on first visit
- ✅ Perfect for personal portfolio/resume

### Tips:
1. **Keep it awake**: Use a service like UptimeRobot to ping your URL every 10 minutes
2. **Custom domain**: You can add your own domain for free
3. **Updates**: Just push to GitHub and Render auto-deploys!

## Troubleshooting

If deployment fails:
1. Check Build Logs in Render dashboard
2. Make sure all files are uploaded correctly
3. Verify requirements.txt includes gunicorn
4. Make sure Procfile has no file extension

## Share Your Resume!
Once deployed, share your link:
- Add to LinkedIn profile
- Include in email signature
- Add to business cards
- Share on social media

Your professional digital resume is now live and accessible worldwide! 🚀
