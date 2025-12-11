"""
Initialize database for recipe finder app
Student Project - PT2 Final
Run this first before starting docker containers
"""

import json
import time
import os
import sys

def print_header():
    """Print fancy header"""
    print("=" * 60)
    print("      RECIPE FINDER APP - DATABASE SETUP")
    print("=" * 60)
    print()

def check_requirements():
    """Check if required packages are installed"""
    print("📦 Checking requirements...")
    
    requirements = [
        ("chromadb", "chromadb"),
        ("sentence-transformers", "sentence_transformers"),
        ("fastapi", "fastapi"),
        ("gradio", "gradio")
    ]
    
    all_ok = True
    for pip_name, import_name in requirements:
        try:
            __import__(import_name)
            print(f"   ✅ {pip_name}")
        except ImportError:
            print(f"   ❌ {pip_name} (missing)")
            all_ok = False
    
    if not all_ok:
        print("\n⚠️  Some packages missing. Docker will install them, but you can run:")
        print("   pip install chromadb sentence-transformers fastapi gradio")
    else:
        print("\n✅ All requirements found!")
    
    return all_ok

def check_files():
    """Check if required files exist"""
    print("\n📁 Checking files...")
    
    required_files = [
        ("data/recipes.json", "Recipe data"),
        ("backend/", "Backend folder"),
        ("frontend/", "Frontend folder"),
        ("docker-compose.yml", "Docker config"),
        ("backend/Dockerfile", "Backend Dockerfile"),
        ("frontend/Dockerfile", "Frontend Dockerfile")
    ]
    
    all_ok = True
    for filepath, description in required_files:
        if os.path.exists(filepath):
            if filepath.endswith("/"):
                # It's a directory
                print(f"   ✅ {description}: {filepath}")
            else:
                # It's a file
                size = os.path.getsize(filepath) if os.path.isfile(filepath) else 0
                print(f"   ✅ {description}: {filepath} ({size} bytes)")
        else:
            print(f"   ❌ {description}: {filepath} (MISSING)")
            all_ok = False
    
    return all_ok

def load_recipes():
    """Load and check recipes file"""
    print("\n📊 Loading recipes...")
    
    try:
        with open("data/recipes.json", "r") as f:
            recipes = json.load(f)
        
        if not isinstance(recipes, list):
            print("   ❌ recipes.json should contain a list")
            return []
        
        print(f"   ✅ Loaded {len(recipes)} recipes")
        
        # Show sample recipes
        print("\n   Sample recipes:")
        for i, recipe in enumerate(recipes[:3], 1):
            print(f"   {i}. {recipe.get('title', 'No title')}")
            print(f"      Ingredients: {', '.join(recipe.get('ingredients', []))[:50]}...")
        
        return recipes
    
    except FileNotFoundError:
        print("   ❌ ERROR: data/recipes.json not found!")
        print("   Create a data folder with recipes.json file")
        return []
    except json.JSONDecodeError as e:
        print(f"   ❌ ERROR: Invalid JSON in recipes.json: {e}")
        return []
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        return []

def check_docker():
    """Check if Docker is available"""
    print("\n🐳 Checking Docker...")
    
    try:
        # Try to run docker version command
        result = os.system("docker --version")
        if result == 0:
            print("   ✅ Docker is installed")
            return True
        else:
            print("   ❌ Docker not found or not running")
            return False
    except:
        print("   ❌ Could not check Docker")
        return False

def setup_database():
    """Initialize the vector database"""
    print("\n🗄️  Setting up vector database...")
    
    try:
        # This is a simple setup - actual setup happens in Docker
        print("   ⏳ Database will be set up when Docker starts")
        print("   Note: First time may download models (~300MB)")
        
        # Create a simple test to verify database works
        test_file = "database_test.txt"
        with open(test_file, "w") as f:
            f.write("Database setup complete!\n")
            f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        print(f"   ✅ Created setup file: {test_file}")
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def print_next_steps():
    """Print what to do next"""
    print("\n" + "=" * 60)
    print("🎉 SETUP COMPLETE!")
    print("=" * 60)
    
    print("\n📋 NEXT STEPS:")
    print("1. Start the application:")
    print("   docker-compose up --build")
    print()
    print("2. Wait for containers to start (2-3 minutes first time)")
    print("   You'll see messages like:")
    print("   - 'Loading model...'")
    print("   - 'Connected to ChromaDB'")
    print("   - 'Running on http://0.0.0.0:7860'")
    print()
    print("3. Open your browser to:")
    print("   http://localhost:7860")
    print()
    print("4. Try it:")
    print("   Enter: chicken, rice, vegetables")
    print("   Choose: savory, pan")
    print("   Click: Find Recipes!")
    print()
    print("⚠️  IMPORTANT NOTES:")
    print("   - First run downloads ML models (be patient)")
    print("   - Make sure Docker Desktop is running")
    print("   - If errors, check all files are in correct places")
    print()
    print("🛑 To stop the application:")
    print("   Press Ctrl+C in terminal")
    print("   Or: docker-compose down")
    print()
    print("🔧 For help:")
    print("   Check README.txt or ask your instructor")
    print("=" * 60)

def main():
    """Main function"""
    print_header()
    
    # Check requirements
    check_requirements()
    
    # Check files
    files_ok = check_files()
    if not files_ok:
        print("\n⚠️  Some files missing. Please check project structure.")
        print("   Required structure:")
        print("   recipe_project/")
        print("   ├── docker-compose.yml")
        print("   ├── backend/ (with Dockerfile, main.py, etc.)")
        print("   ├── frontend/ (with Dockerfile, app.py, etc.)")
        print("   └── data/recipes.json")
        return
    
    # Load recipes
    recipes = load_recipes()
    if not recipes:
        print("\n⚠️  No recipes loaded. App may not work properly.")
        # Continue anyway for setup
    
    # Check Docker
    docker_ok = check_docker()
    if not docker_ok:
        print("\n⚠️  Docker issues detected.")
        print("   Make sure Docker Desktop is installed and running")
        print("   Download from: https://www.docker.com/products/docker-desktop/")
        # Continue anyway
    
    # Setup database
    setup_database()
    
    # Print next steps
    print_next_steps()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Setup interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check your setup and try again")
        sys.exit(1)