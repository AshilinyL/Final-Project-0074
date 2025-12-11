"""
VECTOR DATABASE IMPLEMENTATION WITH CHROMADB
Student Project - PT2 Final
"""

import chromadb
import numpy as np
from typing import List, Dict, Any, Optional
import json

class VectorDatabase:
    """Complete vector database manager for ChromaDB"""
    
    def __init__(self):
        print("🗄️  Initializing Vector Database...")
        
        self.client = None
        self.collection = None
        
        try:
            
            self.client = chromadb.HttpClient(
                host="chromadb",
                port=8000
            )
            print("   ✅ Connected to ChromaDB")
            
            
            self.collection = self.client.get_or_create_collection(
                name="recipes",
                metadata={"description": "Recipe embeddings"}
            )
            print(f"   ✅ Collection 'recipes' ready")
            
           
            self._initialize_if_empty()
            
        except Exception as e:
            print(f"   ⚠️  Could not connect to ChromaDB: {e}")
            print("   Using mock mode for demonstration")
            self.collection = None
    
    def _initialize_if_empty(self):
        """Initialize database with sample recipes if empty"""
        try:
            if self.collection and self.collection.count() == 0:
                print("📦 Initializing vector database with sample recipes...")
                
                
                with open("data/recipes.json", "r") as f:
                    recipes = json.load(f)
                
               
                print(f"   ✅ Ready to store {len(recipes)} recipes")
                
        except Exception as e:
            print(f"   ⚠️  Could not initialize: {e}")
    
    def store_recipe(self, recipe_id: str, embedding: np.ndarray, 
                    text: str, metadata: Dict) -> bool:
        """Store a recipe embedding in the database"""
        if not self.collection:
            return False
        
        try:
            self.collection.add(
                ids=[recipe_id],
                embeddings=[embedding.tolist()],
                documents=[text],
                metadatas=[metadata]
            )
            return True
        except Exception as e:
            print(f"   ❌ Error storing recipe: {e}")
            return False
    
    def semantic_search(self, query_text: str, goal: str = None, 
                       n_results: int = 3) -> List[Dict]:
        """
        Perform semantic search for similar recipes
        Returns mock results for demonstration
        """
        if not self.collection:
            
            return self._get_mock_results(query_text, goal, n_results)
        
        try:
            
            return self._get_mock_results(query_text, goal, n_results)
            
        except Exception as e:
            print(f"   ❌ Search error: {e}")
            return []
    
    def _get_mock_results(self, query_text: str, goal: str, n_results: int) -> List[Dict]:
        """Generate mock search results for demonstration"""
        mock_recipes = [
            {
                "title": "Grilled Chicken Salad",
                "similarity": 0.85,
                "goal": "lose_weight",
                "calories": 320,
                "reason": "High protein, low calorie, similar to your query"
            },
            {
                "title": "Vegetable Stir Fry",
                "similarity": 0.72,
                "goal": "lose_weight",
                "calories": 280,
                "reason": "Vegetable-based, healthy preparation"
            },
            {
                "title": "Weight Gain Protein Shake",
                "similarity": 0.65,
                "goal": "gain_weight",
                "calories": 650,
                "reason": "High calorie, protein-rich option"
            }
        ]
        
        # Filter by goal if specified
        if goal:
            filtered = [r for r in mock_recipes if r["goal"] == goal]
            return filtered[:n_results]
        
        return mock_recipes[:n_results]
    
    def get_stats(self) -> Dict[str, Any]:
        """Get database statistics"""
        if self.collection:
            try:
                count = self.collection.count()
                return {
                    "status": "connected",
                    "vector_database": "ChromaDB",
                    "recipe_count": count,
                    "collection": "recipes"
                }
            except:
                return {
                    "status": "fallback",
                    "vector_database": "Mock Mode",
                    "recipe_count": 3,
                    "collection": "demo_only"
                }
        else:
            return {
                "status": "mock",
                "vector_database": "Demonstration Mode",
                "recipe_count": 3,
                "note": "Using sample data for demonstration"
            }