import dash
from dash import html, dcc
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server  # Expose server for deployment

# Custom CSS styling
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Digital Resume</title>
        {%favicon%}
        {%css%}
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #001f3f 0%, #003d7a 100%);
                min-height: 100vh;
                padding: 40px 20px;
            }
            
            #react-entry-point {
                max-width: 1400px;
                margin: 0 auto;
            }
            
            .page-container {
                display: block;
                width: 100%;
            }
            
            .top-nav {
                background: rgba(255, 255, 255, 0.98);
                backdrop-filter: blur(10px);
                border-radius: 15px;
                padding: 8px 20px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
                width: 100%;
                overflow-x: auto;
            }
            
            .sidebar {
                display: none;
            }
            
            .main-content {
                flex: 1;
                width: 100%;
            }
            
            .main-container {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 60px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                animation: fadeIn 0.8s ease-out;
                margin-bottom: 30px;
                flex: 1;
            }
            
            .two-column-layout {
                display: flex;
                gap: 50px;
                align-items: flex-start;
            }
            
            .left-column {
                flex: 0 0 400px;
                display: flex;
                flex-direction: column;
                gap: 20px;
            }
            
            .right-column {
                flex: 1;
                display: flex;
                align-items: center;
            }
            
            .home-wrapper {
                display: flex;
                gap: 30px;
                align-items: stretch;
            }
            
            .left-container {
                flex: 0 0 450px;
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 50px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                animation: fadeIn 0.8s ease-out;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }
            
            .profile-image {
                width: 200px;
                height: 200px;
                border-radius: 50%;
                object-fit: cover;
                border: 5px solid #001f3f;
                box-shadow: 0 10px 30px rgba(0, 31, 63, 0.3);
                float: right;
                margin-left: 30px;
                margin-bottom: 20px;
                shape-outside: circle();
            }
            
            .profile-placeholder {
                width: 200px;
                height: 200px;
                border-radius: 50%;
                background: linear-gradient(135deg, #001f3f 0%, #003d7a 100%);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 4rem;
                color: white;
                font-weight: 700;
                border: 5px solid #c0c0c0;
                box-shadow: 0 10px 30px rgba(0, 31, 63, 0.3);
                float: right;
                margin-left: 30px;
                margin-bottom: 20px;
                shape-outside: circle();
            }
            
            .right-container {
                flex: 1;
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 50px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                animation: fadeIn 0.8s ease-out;
                display: block;
                position: relative;
            }
            
            .section-card {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 40px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                animation: fadeIn 0.8s ease-out;
                margin-bottom: 30px;
                flex: 1;
            }
            
            h1 {
                font-size: 2.8rem;
                font-weight: 700;
                background: linear-gradient(135deg, #001f3f 0%, #c0c0c0 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                margin-bottom: 20px;
                text-align: left;
                letter-spacing: 2px;
                text-transform: uppercase;
            }
            
            .header-flex {
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
                margin-bottom: 10px;
            }
            
            .name-section {
                flex: 1;
            }
            
            .linkedin-square {
                background: linear-gradient(135deg, #001f3f 0%, #003d7a 100%);
                color: white;
                padding: 15px 20px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: 600;
                box-shadow: 0 8px 20px rgba(0, 31, 63, 0.3);
                transition: all 0.3s ease;
                font-family: 'Poppins', sans-serif;
                display: inline-flex;
                align-items: center;
                gap: 8px;
                font-size: 1rem;
                width: fit-content;
            }
            
            .linkedin-square:hover {
                transform: translateY(-3px);
                box-shadow: 0 12px 30px rgba(0, 61, 122, 0.5);
                background: linear-gradient(135deg, #003d7a 0%, #004d99 100%);
            }
            
            p {
                font-size: 1.25rem;
                color: #444;
                text-align: center;
                font-weight: 400;
                line-height: 1.6;
                letter-spacing: 0.5px;
            }
            
            .professional-title {
                font-size: 1rem;
                line-height: 1.8;
                letter-spacing: 2px;
                text-transform: uppercase;
                font-weight: 500;
                color: #003d7a;
                margin-bottom: 25px;
            }
            
            .experience-badge {
                display: inline-block;
                background: linear-gradient(135deg, #001f3f 0%, #003d7a 100%);
                color: white;
                padding: 12px 30px;
                border-radius: 50px;
                font-size: 1rem;
                font-weight: 600;
                margin: 0;
                box-shadow: 0 8px 25px rgba(0, 31, 63, 0.4);
                animation: pulse 2s ease-in-out infinite;
                cursor: pointer;
                transition: transform 0.3s ease;
            }
            
            .experience-badge:hover {
                transform: scale(1.05);
            }
            
            .experience-badge-container {
                text-align: center;
                margin: 30px 0;
            }
            
            @keyframes pulse {
                0%, 100% {
                    transform: scale(1);
                    box-shadow: 0 10px 30px rgba(0, 31, 63, 0.4);
                }
                50% {
                    transform: scale(1.05);
                    box-shadow: 0 15px 40px rgba(0, 61, 122, 0.6);
                }
            }
            
            .summary-text {
                font-size: 1.15rem;
                line-height: 2;
                color: #2c3e50;
                text-align: justify;
                font-weight: 400;
                letter-spacing: 0.3px;
                margin: 0;
            }
            
            /* Button Styles */
            .button-container {
                display: flex;
                flex-direction: row;
                gap: 5px;
                padding: 0;
                background: transparent;
                border: none;
                box-shadow: none;
                backdrop-filter: none;
                justify-content: space-evenly;
                align-items: center;
                flex-wrap: nowrap;
                width: 100%;
            }
            
            .nav-button {
                background: transparent;
                color: #8b95a5;
                border: none;
                padding: 8px 12px;
                font-size: 0.6rem;
                font-weight: 500;
                border-radius: 8px;
                cursor: pointer;
                box-shadow: none;
                transition: all 0.3s ease;
                font-family: 'Poppins', sans-serif;
                text-align: center;
                text-decoration: none;
                display: inline-flex;
                flex-direction: column;
                align-items: center;
                gap: 4px;
                backdrop-filter: none;
                opacity: 1;
                text-transform: uppercase;
                letter-spacing: 1px;
                min-width: 80px;
                white-space: nowrap;
                flex-shrink: 0;
            }
            
            .nav-button:hover {
                background: rgba(0, 31, 63, 0.05);
                color: #001f3f;
            }
            
            .nav-button:hover .nav-icon {
                color: #001f3f;
                transform: scale(1.1);
            }
            
            .nav-icon {
                font-size: 1.2rem;
                display: block;
                margin-bottom: 2px;
                line-height: 1;
                color: #8b95a5;
                transition: all 0.3s ease;
            }
            
            .nav-button:active {
                transform: translateY(-1px);
            }
            
            /* Collapsible Section Styles */
            .section-content {
                padding: 20px;
                background: linear-gradient(135deg, rgba(0, 31, 63, 0.05) 0%, rgba(192, 192, 192, 0.1) 100%);
                border-radius: 15px;
                border-left: 5px solid #c0c0c0;
            }
            
            .section-title-header {
                font-size: 2rem;
                font-weight: 700;
                color: #001f3f;
                margin-bottom: 25px;
                letter-spacing: 0.5px;
            }
            
            .content-text {
                font-size: 1.05rem;
                line-height: 2;
                color: #2c3e50;
                margin-bottom: 10px;
                letter-spacing: 0.3px;
            }
            
            /* Responsive Design */
            
            @media (max-width: 768px) {
                .button-container {
                    gap: 5px;
                    justify-content: flex-start;
                }
                
                .nav-button {
                    padding: 12px 10px;
                    font-size: 0.6rem;
                    min-width: 70px;
                }
                
                .nav-icon {
                    font-size: 1.2rem;
                }
                
                .top-nav {
                    padding: 15px;
                }
                
                .home-wrapper {
                    flex-direction: column;
                    gap: 20px;
                }
                
                .left-container {
                    flex: 1;
                    width: 100%;
                }
                
                .right-container {
                    flex: 1;
                    width: 100%;
                }
                
                .profile-image,
                .profile-placeholder {
                    width: 150px;
                    height: 150px;
                    font-size: 3rem;
                    float: none;
                    margin: 0 auto 20px auto;
                    display: flex;
                }
                
                .summary-text {
                    text-align: left;
                }
                
                h1 {
                    font-size: 2.5rem;
                    text-align: center !important;
                }
                
                .linkedin-square {
                    align-self: center;
                }
            }
            
            @keyframes fadeIn {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            /* Decorative elements */
            .main-container::before {
                content: '';
                position: absolute;
                top: -2px;
                left: -2px;
                right: -2px;
                bottom: -2px;
                background: linear-gradient(135deg, #001f3f 0%, #003d7a 100%);
                border-radius: 20px;
                z-index: -1;
                opacity: 0.1;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Define page layouts
home_layout = html.Div([
    # LEFT CONTAINER - Personal Info
    html.Div([
        html.H1("Guram Magularia", style={'textAlign': 'center'}),
        html.P("Legal Counsel | Civil & Legal Law | Contract & Real Estate Law", 
               className="professional-title", style={'textAlign': 'center'}),
        
        # Experience Badge
        html.Div([
            dcc.Link("5+ Years of Experience", href="/experience", className="experience-badge", 
                    style={'textDecoration': 'none', 'color': 'white'})
        ], style={'textAlign': 'center', 'marginBottom': '20px'}),
        
        # LinkedIn Button
        html.Div([
            html.A([
                html.I(className="fab fa-linkedin", style={'fontSize': '1.2rem'}),
                html.Span("Connect on LinkedIn")
            ], 
            href="https://www.linkedin.com/in/guram-magularia-20215b18a/", 
            target="_blank",
            className="linkedin-square"
            )
        ], style={'textAlign': 'center'})
    ], className="left-container"),
    
    # RIGHT CONTAINER - Profile Image and Summary
    html.Div([
        # Profile Image
        html.Img(src='/assets/photo.jpg', className="profile-image"),
        
        html.Div(
            "Highly experienced Legal Counsel with expertise in civil law, contract law, business law, and real estate law. "
            "Proven ability to handle complex legal matters, negotiate high-value agreements, and ensure regulatory compliance. "
            "Skilled in leading legal teams, advising top-tier real estate developers, and mitigating legal risks in dynamic business environments. "
            "A strategic thinker with strong problem-solving skills and a track record of delivering practical legal solutions.",
            className="summary-text"
        )
    ], className="right-container")
], className="home-wrapper")

contact_layout = html.Div([
    html.H3("Contact Information", className="section-title-header"),
    html.Div([
        html.P("📧 Email: Magulariaguram@gmail.com", className="content-text"),
        html.P("📱 Phone: +995 595 41 77 75", className="content-text"),
        html.P("📍 Location: Georgia, Batumi, Melikishvili street N10", className="content-text"),
        html.P("💼 LinkedIn: linkedin.com/in/guram-magularia-20215b18a", className="content-text"),
    ], className="section-content")
], className="section-card")

education_layout = html.Div([
    html.H3("Education", className="section-title-header"),
    html.Div([
        html.P("🎓 Master of Laws (LL.M.)", className="content-text", style={'fontWeight': '600', 'fontSize': '1.15rem', 'color': '#001f3f'}),
        html.P("Caucasus University - Tbilisi, Georgia", className="content-text"),
        html.P("📅 2020 - 2023", className="content-text", style={'marginBottom': '25px'}),
        
        html.P("🎓 Bachelor of Laws", className="content-text", style={'fontWeight': '600', 'fontSize': '1.15rem', 'color': '#001f3f'}),
        html.P("Georgian Technical University - Tbilisi, Georgia", className="content-text"),
        html.P("📅 2015 - 2019", className="content-text"),
    ], className="section-content")
], className="section-card")

experience_layout = html.Div([
    html.H3("Work Experience", className="section-title-header"),
    html.Div([
        # NEXT Position
        html.P("💼 Leading Lawyer", className="content-text", style={'fontWeight': '600', 'fontSize': '1.15rem', 'color': '#001f3f'}),
        html.P("Real Estate Developer Company - NEXT", className="content-text", style={'fontWeight': '600'}),
        html.P("📅 2021 - Present", className="content-text", style={'marginBottom': '10px'}),
        html.P("• Led the legal department of a top real estate development company, providing expert guidance on contractual, regulatory, and dispute resolution matters.", className="content-text"),
        html.P("• Negotiated and drafted high-value contracts, ensuring compliance with Georgian and international legal standards.", className="content-text"),
        html.P("• Managed litigation and dispute resolution processes, minimizing company risks and financial exposure.", className="content-text"),
        html.P("• Advised executive leadership on legal strategies, compliance, and business expansion initiatives.", className="content-text"),
        html.P("• Successfully handled legal due diligence for multi-million-dollar real estate transactions.", className="content-text", style={'marginBottom': '30px'}),
        
        # PASHA BANK Position
        html.P("💼 Litigation Lawyer", className="content-text", style={'fontWeight': '600', 'fontSize': '1.15rem', 'color': '#001f3f'}),
        html.P("PASHA BANK GEORGIA", className="content-text", style={'fontWeight': '600'}),
        html.P("📅 2021", className="content-text", style={'marginBottom': '10px'}),
        html.P("• Established and led the bank's litigation system.", className="content-text"),
        html.P("• Managed legal disputes and enforcement proceedings.", className="content-text"),
        html.P("• Advised management on litigation risks and strategies.", className="content-text", style={'marginBottom': '30px'}),
        
        # FINCA BANK Position
        html.P("💼 Lawyer", className="content-text", style={'fontWeight': '600', 'fontSize': '1.15rem', 'color': '#001f3f'}),
        html.P("FINCA BANK GEORGIA", className="content-text", style={'fontWeight': '600'}),
        html.P("📅 2019 - 2021", className="content-text", style={'marginBottom': '10px'}),
        html.P("• Represented the bank in court proceedings and in administrative bodies.", className="content-text"),
        html.P("• Negotiated settlements and agreements with clients.", className="content-text", style={'marginBottom': '30px'}),
        
        # Tbilisi City Court Internship
        html.P("💼 Intern", className="content-text", style={'fontWeight': '600', 'fontSize': '1.15rem', 'color': '#001f3f'}),
        html.P("Tbilisi City Court", className="content-text", style={'fontWeight': '600'}),
        html.P("📅 2018 - 2019", className="content-text", style={'marginBottom': '10px'}),
        html.P("• Assisted the judge and judicial assistant in case proceedings.", className="content-text"),
        html.P("• Recorded legal documents and drafted court decisions.", className="content-text"),
        html.P("• Performed various procedural and administrative tasks.", className="content-text"),
    ], className="section-content")
], className="section-card")

languages_layout = html.Div([
    html.H3("Languages", className="section-title-header"),
    html.Div([
        html.P("🇬🇪 Georgian – Native", className="content-text"),
        html.P("🇬🇧 English – B2 (Upper Intermediate)", className="content-text"),
        html.P("🇷🇺 Russian – C1 (Advanced)", className="content-text"),
        html.P("🇮🇹 Italian – A2 (Basic proficiency, ongoing learning)", className="content-text"),
    ], className="section-content")
], className="section-card")

skills_layout = html.Div([
    html.H3("Professional Skills", className="section-title-header"),
    html.Div([
        html.P("⚖️ Contract Drafting & Negotiation", className="content-text", style={'fontWeight': '500'}),
        html.P("📋 Civil & Business Law", className="content-text", style={'fontWeight': '500'}),
        html.P("🏢 Real Estate & Construction Law", className="content-text", style={'fontWeight': '500'}),
        html.P("🛡️ Legal Risk Management", className="content-text", style={'fontWeight': '500'}),
        html.P("✅ Regulatory Compliance", className="content-text", style={'fontWeight': '500'}),
        html.P("🏛️ Corporate Governance", className="content-text", style={'fontWeight': '500'}),
        html.P("⚡ Dispute Resolution & Litigation", className="content-text", style={'fontWeight': '500'}),
        html.P("👥 Team Leadership & Legal Strategy", className="content-text", style={'fontWeight': '500'}),
    ], className="section-content")
], className="section-card")

licenses_layout = html.Div([
    html.H3("Licenses & Certificates", className="section-title-header"),
    html.Div([
        html.P("📜 Member of the Georgian Bar Association", className="content-text", style={'fontWeight': '600', 'fontSize': '1.15rem', 'color': '#001f3f'}),
        html.P("Attorney in civil and administrative matters", className="content-text", style={'marginBottom': '25px'}),
        
        html.P("🎓 Professional Certifications:", className="content-text", style={'fontWeight': '600', 'fontSize': '1.1rem', 'marginBottom': '10px'}),
        html.P("• Certified in Construction Law", className="content-text"),
        html.P("• Certified in Intellectual Property", className="content-text"),
        html.P("• Certified in Personal Data Protection", className="content-text"),
        html.P("• Certified in Public Speaking & Debate", className="content-text"),
    ], className="section-content")
], className="section-card")

# News Layout
news_layout = html.Div([
    html.H3("News & Updates", className="section-title-header"),
    html.Div([
        html.P("🎉 Happy Birthday Milan! 🎂", className="content-text", style={'fontWeight': '600', 'fontSize': '1.5rem', 'color': '#001f3f', 'textAlign': 'center', 'marginBottom': '30px'}),
        
        # AC Milan Birthday Quiz
        html.Div([
            html.P("⚽ Quiz Time! When is AC Milan's Birthday?", className="content-text", style={'fontWeight': '600', 'fontSize': '1.3rem', 'color': '#001f3f', 'textAlign': 'center', 'marginBottom': '20px'}),
            
            dcc.RadioItems(
                id='milan-quiz',
                options=[
                    {'label': ' December 16, 1898', 'value': '1'},
                    {'label': ' December 15, 1898', 'value': '2'},
                    {'label': ' December 16, 1899', 'value': '3'},
                    {'label': ' December 15, 1899', 'value': '4'}
                ],
                style={'fontSize': '1.1rem', 'marginBottom': '20px'},
                labelStyle={'display': 'block', 'marginBottom': '15px', 'cursor': 'pointer'}
            ),
            
            html.Div(id='quiz-result', style={'fontSize': '1.2rem', 'fontWeight': '600', 'textAlign': 'center', 'marginTop': '20px', 'padding': '20px', 'borderRadius': '10px'})
        ], style={'background': 'rgba(0, 31, 63, 0.05)', 'padding': '30px', 'borderRadius': '15px', 'marginBottom': '30px'}),
        
        html.P("📰 Recent Updates", className="content-text", style={'fontWeight': '600', 'fontSize': '1.2rem', 'color': '#001f3f', 'marginBottom': '20px'}),
        
        html.P("🏆 Achievement 1", className="content-text", style={'fontWeight': '600', 'fontSize': '1.1rem', 'color': '#001f3f'}),
        html.P("📅 December 2024", className="content-text", style={'marginBottom': '10px'}),
        html.P("Description of your recent achievement or news item.", className="content-text", style={'marginBottom': '25px'}),
        
        html.P("🏆 Achievement 2", className="content-text", style={'fontWeight': '600', 'fontSize': '1.1rem', 'color': '#001f3f'}),
        html.P("📅 November 2024", className="content-text", style={'marginBottom': '10px'}),
        html.P("Another recent news or achievement.", className="content-text", style={'marginBottom': '25px'}),
        
        html.P("🏆 Achievement 3", className="content-text", style={'fontWeight': '600', 'fontSize': '1.1rem', 'color': '#001f3f'}),
        html.P("📅 October 2024", className="content-text", style={'marginBottom': '10px'}),
        html.P("More updates and news.", className="content-text"),
    ], className="section-content")
], className="section-card")

# Define the main layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    
    # Top Navigation Bar
    html.Div([
        html.Div([
            dcc.Link([html.I(className="fas fa-home nav-icon"), "Home"], href="/", className="nav-button"),
            dcc.Link([html.I(className="fas fa-envelope nav-icon"), "Contact"], href="/contact", className="nav-button"),
            dcc.Link([html.I(className="fas fa-graduation-cap nav-icon"), "Education"], href="/education", className="nav-button"),
            dcc.Link([html.I(className="fas fa-briefcase nav-icon"), "Experience"], href="/experience", className="nav-button"),
            dcc.Link([html.I(className="fas fa-star nav-icon"), "Skills"], href="/skills", className="nav-button"),
            dcc.Link([html.I(className="fas fa-globe nav-icon"), "Languages"], href="/languages", className="nav-button"),
            dcc.Link([html.I(className="fas fa-certificate nav-icon"), "Licenses"], href="/licenses", className="nav-button"),
            dcc.Link([html.I(className="fas fa-newspaper nav-icon"), "News"], href="/news", className="nav-button"),
        ], className="button-container")
    ], className="top-nav"),
    
    html.Div([
        # Main Content
        html.Div(id='page-content', className='main-content')
        
    ], className="page-container")
])

# Callback for page routing
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/contact':
        return contact_layout
    elif pathname == '/education':
        return education_layout
    elif pathname == '/experience':
        return experience_layout
    elif pathname == '/skills':
        return skills_layout
    elif pathname == '/languages':
        return languages_layout
    elif pathname == '/licenses':
        return licenses_layout
    elif pathname == '/news':
        return news_layout
    else:
        return home_layout

# Callback for AC Milan Birthday Quiz
@app.callback(
    Output('quiz-result', 'children'),
    Output('quiz-result', 'style'),
    Input('milan-quiz', 'value')
)
def check_quiz_answer(answer):
    if answer is None:
        return "", {'display': 'none'}
    
    if answer == '3':
        return "⚽ Guga is Proud Of You! 🎉", {
            'fontSize': '1.3rem',
            'fontWeight': '600',
            'textAlign': 'center',
            'marginTop': '20px',
            'padding': '20px',
            'borderRadius': '10px',
            'background': 'linear-gradient(135deg, #00c853 0%, #00e676 100%)',
            'color': 'white',
            'boxShadow': '0 10px 30px rgba(0, 200, 83, 0.3)'
        }
    else:
        return "❌ Guga is not happy with your answer, you can not try again 😔", {
            'fontSize': '1.2rem',
            'fontWeight': '600',
            'textAlign': 'center',
            'marginTop': '20px',
            'padding': '20px',
            'borderRadius': '10px',
            'background': 'linear-gradient(135deg, #d32f2f 0%, #f44336 100%)',
            'color': 'white',
            'boxShadow': '0 10px 30px rgba(211, 47, 47, 0.3)'
        }

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
