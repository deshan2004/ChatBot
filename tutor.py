
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from datetime import datetime
import random
from knowledge_base import load_knowledge_base, get_concept_by_level, get_concept_by_category, search_concepts, get_learning_path
from quiz_data import load_quiz_questions

class ProgrammingTutor:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 LearnBot - Your Programming Companion")
        self.root.geometry("1200x800")
        self.root.configure(bg='#e6f2ff') 
        
        self.colors = {
            'bg_dark': '#e6f2ff',        
            'bg_light': '#ffffff',     
            'accent': '#1976d2',         
            'accent_light': '#42a5f5',   
            'success': '#388e3c',      
            'warning': '#f57c00',        
            'danger': '#d32f2f',        
            'text_light': '#ffffff',     
            'text_dark': '#1a237e',      
            'highlight': '#ffd54f',      
            'sidebar': '#bbdefb',       
            'chat_bg': '#f5f9ff',       
            'input_bg': '#ffffff',     
            'input_border': '#90caf9',  
            'placeholder': '#9e9e9e'   
        }
        
        self.concepts = load_knowledge_base()
        self.quiz_questions = load_quiz_questions()
        self.user_progress = {
            'concepts_learned': [], 
            'quiz_scores': [], 
            'session_start': datetime.now()
        }
        
        self.quiz_active = False
        self.current_question = 0
        self.quiz_score = 0
        
        self.setup_ui()
        
    def setup_ui(self):
        self.configure_styles()
        
        main_container = tk.Frame(self.root, bg=self.colors['bg_dark'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        header_frame = tk.Frame(main_container, bg=self.colors['accent'], height=100)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, 
                             text="🤖 LearnBot - Your Programming Companion", 
                             font=('Arial', 20, 'bold'),
                             bg=self.colors['accent'],
                             fg=self.colors['text_light'],
                             pady=20)
        title_label.pack(expand=True)
        
        subtitle_label = tk.Label(header_frame,
                                text="Making programming concepts easy and accessible for everyone",
                                font=('Arial', 11),
                                bg=self.colors['accent'],
                                fg=self.colors['text_light'])
        subtitle_label.pack()
        
        content_frame = tk.Frame(main_container, bg=self.colors['bg_dark'])
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        left_panel = tk.Frame(content_frame, bg=self.colors['sidebar'], width=300)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        left_panel.pack_propagate(False)
        
        right_panel = tk.Frame(content_frame, bg=self.colors['bg_dark'])
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        left_title = tk.Label(left_panel, text="📚 Learning Topics", 
                            font=('Arial', 16, 'bold'),
                            bg=self.colors['sidebar'],
                            fg=self.colors['text_dark'],
                            pady=15)
        left_title.pack(fill=tk.X)
        
        categories = [
            ("🎯 Core Concepts", ["variables", "data types", "functions", "conditionals", "loops", "arrays"]),
            ("⚡ Programming Techniques", ["algorithms", "recursion", "debugging", "pseudocode", "flowcharts"]),
            ("🏗️ Advanced Topics", ["data structures"]),
            ("🔍 Algorithms Deep Dive", ["sorting algorithms", "searching algorithms", "binary search", "bubble sort", "quick sort"])
        ]
        
        for category_name, concepts_list in categories:
            category_frame = tk.Frame(left_panel, bg=self.colors['sidebar'])
            category_frame.pack(fill=tk.X, padx=15, pady=8)
            
            category_label = tk.Label(category_frame, text=category_name,
                                    font=('Arial', 12, 'bold'),
                                    bg=self.colors['sidebar'],
                                    fg=self.colors['accent'],
                                    anchor='w')
            category_label.pack(fill=tk.X)
            
            for concept in concepts_list:
                btn = tk.Button(category_frame, 
                              text=f"  {self.concepts[concept].get('icon', '📖')} {concept.title()}",
                              command=lambda c=concept: self.explain_concept(c),
                              font=('Arial', 10),
                              bg=self.colors['bg_light'],
                              fg=self.colors['text_dark'],
                              relief='flat',
                              anchor='w',
                              padx=12,
                              pady=6,
                              bd=1)
                btn.pack(fill=tk.X, pady=2)
                self.create_hover_effect(btn, self.colors['bg_light'], self.colors['accent_light'])
        
        action_frame = tk.Frame(left_panel, bg=self.colors['sidebar'])
        action_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=15)
        
        actions = [
            ("📝 Take Quiz", self.start_quiz, self.colors['success']),
            ("❓ Get Help", self.show_help, self.colors['warning']),
            ("📈 My Progress", self.show_progress, self.colors['accent']),
            ("🗑️ Clear Chat", self.clear_chat, self.colors['danger'])
        ]
        
        for text, command, color in actions:
            btn = tk.Button(action_frame, text=text, command=command,
                          font=('Arial', 11, 'bold'),
                          bg=color,
                          fg=self.colors['text_light'],
                          relief='raised',
                          pady=10,
                          bd=2)
            btn.pack(fill=tk.X, padx=10, pady=6)
            self.create_hover_effect(btn, color, self.lighten_color(color))
        
        chat_frame = tk.Frame(right_panel, bg=self.colors['bg_dark'])
        chat_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.chat_display = scrolledtext.ScrolledText(chat_frame, 
                                                    width=80, 
                                                    height=25,
                                                    font=('Arial', 11),
                                                    bg=self.colors['chat_bg'],
                                                    fg=self.colors['text_dark'],
                                                    insertbackground='#1976d2',
                                                    selectbackground=self.colors['accent_light'],
                                                    wrap=tk.WORD,
                                                    padx=15,
                                                    pady=15,
                                                    relief='flat',
                                                    borderwidth=1)
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        self.chat_display.config(state=tk.DISABLED)
        
        input_frame = tk.Frame(right_panel, bg=self.colors['bg_dark'])
        input_frame.pack(fill=tk.X)
        
        input_label = tk.Label(input_frame, text="💬 Ask me anything about programming:", 
                              font=('Arial', 10, 'bold'),
                              bg=self.colors['bg_dark'],
                              fg=self.colors['text_dark'])
        input_label.pack(anchor='w', pady=(0, 8))
        
        input_container = tk.Frame(input_frame, bg=self.colors['bg_dark'])
        input_container.pack(fill=tk.X)
        
        input_field_frame = tk.Frame(input_container, 
                                   bg=self.colors['input_border'],
                                   bd=1,
                                   relief='solid',
                                   padx=2,
                                   pady=2)
        input_field_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        self.user_input = tk.Entry(input_field_frame, 
                                 font=('Arial', 12),
                                 bg=self.colors['input_bg'],
                                 fg=self.colors['text_dark'],
                                 insertbackground='#1976d2',
                                 relief='flat',
                                 borderwidth=0,
                                 width=50)
        self.user_input.pack(fill=tk.X, expand=True, ipady=8)
        
        self.user_input.insert(0, "Type your question here...")
        self.user_input.config(fg=self.colors['placeholder'])
        
        self.user_input.bind('<FocusIn>', self.on_input_focus_in)
        self.user_input.bind('<FocusOut>', self.on_input_focus_out)
        
        self.user_input.bind('<Return>', lambda e: self.process_input())
        
        send_btn = tk.Button(input_container, 
                           text="Send 🚀", 
                           command=self.process_input,
                           font=('Arial', 11, 'bold'),
                           bg=self.colors['accent'],
                           fg=self.colors['text_light'],
                           relief='raised',
                           padx=25,
                           pady=10,
                           bd=0,
                           cursor='hand2')
        send_btn.pack(side=tk.RIGHT)
        self.create_hover_effect(send_btn, self.colors['accent'], self.colors['accent_light'])
        
        self.add_quick_suggestions(input_frame)
        
        self.user_input.focus()
        
        self.display_welcome_message()
    
    def add_quick_suggestions(self, parent_frame):
        """Add quick suggestion buttons below the input field"""
        suggestions_frame = tk.Frame(parent_frame, bg=self.colors['bg_dark'])
        suggestions_frame.pack(fill=tk.X, pady=(10, 0))
        
        suggestions_label = tk.Label(suggestions_frame, 
                                   text="💡 Quick questions:",
                                   font=('Arial', 9),
                                   bg=self.colors['bg_dark'],
                                   fg=self.colors['text_dark'])
        suggestions_label.pack(anchor='w', pady=(0, 5))
        
        suggestions_container = tk.Frame(suggestions_frame, bg=self.colors['bg_dark'])
        suggestions_container.pack(fill=tk.X)
        
        quick_questions = [
            "What are variables?",
            "Explain functions",
            "How do loops work?",
            "Start quiz"
        ]
        
        for question in quick_questions:
            btn = tk.Button(suggestions_container,
                          text=question,
                          command=lambda q=question: self.insert_quick_question(q),
                          font=('Arial', 9),
                          bg=self.colors['bg_light'],
                          fg=self.colors['accent'],
                          relief='flat',
                          padx=12,
                          pady=4,
                          bd=1)
            btn.pack(side=tk.LEFT, padx=(0, 8))
            self.create_hover_effect(btn, self.colors['bg_light'], self.colors['accent_light'])
    
    def insert_quick_question(self, question):
        """Insert a quick question into the input field"""
        self.user_input.delete(0, tk.END)
        self.user_input.config(fg=self.colors['text_dark'])
        self.user_input.insert(0, question)
        self.user_input.focus()
    
    def on_input_focus_in(self, event):
        """Handle focus in event for input field"""
        if self.user_input.get() == "Type your question here...":
            self.user_input.delete(0, tk.END)
            self.user_input.config(fg=self.colors['text_dark'])
    
    def on_input_focus_out(self, event):
        """Handle focus out event for input field"""
        if not self.user_input.get():
            self.user_input.insert(0, "Type your question here...")
            self.user_input.config(fg=self.colors['placeholder'])
    
    def configure_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('Custom.TButton', 
                       background=self.colors['accent'],
                       foreground=self.colors['text_light'],
                       focuscolor='none')
    
    def create_hover_effect(self, widget, normal_color, hover_color):
        widget.bind("<Enter>", lambda e: widget.config(bg=hover_color, cursor='hand2'))
        widget.bind("<Leave>", lambda e: widget.config(bg=normal_color))
    
    def lighten_color(self, color, factor=0.2):
        color_map = {
            self.colors['accent']: '#42a5f5',
            self.colors['success']: '#4caf50',
            self.colors['warning']: '#ff9800',
            self.colors['danger']: '#f44336',
            self.colors['bg_light']: '#e3f2fd'
        }
        return color_map.get(color, color)
    
    def display_welcome_message(self):
        welcome_text = """


Hello there! I'm LearnBot, your friendly programming companion. 
I'm here to make learning programming concepts simple, clear, and enjoyable!


Ready to begin your programming adventure? Let's start learning! 🎯
"""
        self.display_message("🤖 LearnBot", welcome_text, "welcome")
    
    def display_message(self, sender, message, msg_type="normal"):
        self.chat_display.config(state=tk.NORMAL)
        
        if not hasattr(self, 'tags_configured'):
            self.chat_display.tag_configure('welcome', foreground='#1565c0', font=('Arial', 11, 'bold'))
            self.chat_display.tag_configure('bot', foreground='#1976d2', font=('Arial', 11, 'bold'))
            self.chat_display.tag_configure('user', foreground='#388e3c', font=('Arial', 11, 'bold'))
            self.chat_display.tag_configure('system', foreground='#7b1fa2', font=('Arial', 10))
            self.chat_display.tag_configure('success', foreground='#388e3c')
            self.chat_display.tag_configure('error', foreground='#d32f2f')
            self.chat_display.tag_configure('concept', foreground='#f57c00', font=('Arial', 11, 'bold'))
            self.chat_display.tag_configure('code', foreground='#c2185b', font=('Consolas', 10))
            self.tags_configured = True
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.chat_display.insert(tk.END, f"\n[{timestamp}] ", 'system')
        
        if msg_type == "welcome":
            tag = 'welcome'
        elif sender == "🤖 LearnBot":
            tag = 'bot'
        else:
            tag = 'user'
        
        self.chat_display.insert(tk.END, f"{sender}:\n", tag)
        self.chat_display.insert(tk.END, f"{message}\n")
        self.chat_display.insert(tk.END, "─" * 70 + "\n", 'system')
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def process_input(self):
        text = self.user_input.get().strip()
        
        if text == "Type your question here...":
            self.user_input.delete(0, tk.END)
            return
            
        if not text:
            return
        
        self.display_message("👤 You", text, "user")
        self.user_input.delete(0, tk.END)
        
        text_lower = text.lower()
        
        if self.quiz_active:
            self.check_quiz_answer(text)
            return
        
        response = self.generate_response(text_lower)
        self.display_message("🤖 LearnBot", response, "bot")
    
    def generate_response(self, text):
        if any(word in text for word in ['hello', 'hi', 'hey', 'hola', 'namaste']):
            return "👋 Hello! I'm LearnBot, ready to help you explore programming concepts. What would you like to learn about today? Feel free to click the topic buttons or ask me anything!"
        
        elif any(word in text for word in ['bye', 'goodbye', 'exit', 'quit']):
            return "👋 Thanks for learning with LearnBot! Remember, programming is a journey - every step counts. Come back anytime to continue learning! 🚀"
        
        elif any(word in text for word in ['thank', 'thanks', 'appreciate']):
            return "😊 You're very welcome! I'm happy to help you learn. Keep asking questions - that's how great programmers are made! 💪"
        
        elif any(word in text for word in ['quiz', 'test', 'exam']):
            self.start_quiz()
            return ""
        
        elif any(word in text for word in ['progress', 'stats', 'score']):
            self.show_progress()
            return ""
        
        elif any(word in text for word in ['help', 'guide', 'how to']):
            self.show_help()
            return ""
        
        for concept, data in self.concepts.items():
            if any(keyword in text for keyword in self.get_concept_keywords(concept)):
                return self.format_concept_explanation(concept, data)
        
        return self.get_creative_response(text)
    
    def get_concept_keywords(self, concept):
        keywords = [concept]
        if concept == "variables":
            keywords.extend(['var', 'variable', 'storage'])
        elif concept == "data types":
            keywords.extend(['datatype', 'type', 'integer', 'string', 'boolean'])
        elif concept == "loops":
            keywords.extend(['loop', 'for', 'while', 'repeat'])
        elif concept == "functions":
            keywords.extend(['function', 'def', 'method', 'procedure'])
        elif concept == "conditionals":
            keywords.extend(['if', 'else', 'conditional', 'decision'])
        elif concept == "arrays":
            keywords.extend(['array', 'list', 'collection'])
        elif concept == "algorithms":
            keywords.extend(['algorithm', 'step', 'procedure'])
        elif concept == "sorting algorithms":
            keywords.extend(['sort', 'bubble', 'quick', 'merge'])
        elif concept == "searching algorithms":
            keywords.extend(['search', 'binary', 'linear'])
        elif concept == "recursion":
            keywords.extend(['recursive', 'recursion'])
        elif concept == "data structures":
            keywords.extend(['stack', 'queue', 'linked list', 'tree'])
        elif concept == "debugging":
            keywords.extend(['debug', 'error', 'fix'])
        elif concept == "pseudocode":
            keywords.extend(['pseudo', 'algorithm design'])
        elif concept == "flowcharts":
            keywords.extend(['flowchart', 'diagram'])
        elif concept == "binary search":
            keywords.extend(['binary', 'search algorithm'])
        elif concept == "bubble sort":
            keywords.extend(['bubble', 'sorting'])
        elif concept == "quick sort":
            keywords.extend(['quick', 'sorting'])
        return keywords
    
    def format_concept_explanation(self, concept, data):
        icon = data.get('icon', '📚')
        explanation = f"{icon} **{concept.upper()}** {icon}\n\n"
        explanation += f"🎯 **What is it?**\n{data['definition']}\n\n"
        explanation += f"💡 **In simple terms:**\n{data['explanation']}\n\n"
        
        examples = data['example']
        if isinstance(examples, dict):
            explanation += f"📝 **Basic Example:**\n```python\n{examples['basic']}\n```\n\n"
            explanation += f"🚀 **Advanced Example:**\n```python\n{examples['advanced']}\n```\n\n"
        else:
            explanation += f"📝 **Example:**\n```python\n{examples}\n```\n\n"
        
        explanation += f"🔍 **Think of it like this:**\n{data['analogy']}\n\n"
        
        if 'quick_tip' in data:
            explanation += f"💡 **Quick Tip:** {data['quick_tip']}\n\n"
        
        if 'common_mistakes' in data and data['common_mistakes']:
            explanation += f"⚠️ **Common Mistakes:**\n"
            for mistake in data['common_mistakes']:
                explanation += f"   • {mistake}\n"
            explanation += "\n"
        
        if 'practice_exercise' in data:
            explanation += f"🎯 **Try This:** {data['practice_exercise']}\n\n"
        
        if concept not in self.user_progress['concepts_learned']:
            self.user_progress['concepts_learned'].append(concept)
            explanation += f"✅ **Great job!** You've learned about {concept}! 🎉\n"
        
        explanation += "━" * 50
        return explanation
    
    def get_creative_response(self, text):
        responses = [
            "🤔 That's an interesting question! Could you try rephrasing it or ask about specific programming concepts?",
            "🎯 I'm here to help with programming concepts! Try asking about variables, loops, algorithms, or click the topic buttons on the left!",
            "💡 Want to learn something new? How about exploring algorithms or data structures? They're fundamental to programming!",
            "🚀 Great question! I specialize in programming concepts. Try asking about specific topics like 'functions' or 'OOP'!",
            "📚 I'd love to help! Could you be more specific? For example, 'What are functions?' or 'Explain loops'?"
        ]
        return random.choice(responses)
    
    def explain_concept(self, concept):
        if concept in self.concepts:
            data = self.concepts[concept]
            explanation = self.format_concept_explanation(concept, data)
            self.display_message("🤖 LearnBot", explanation, "bot")
        else:
            self.display_message("🤖 LearnBot", f"❌ I don't have information about '{concept}' yet. Try one of the available topics!", "error")
    
    def start_quiz(self):
        self.quiz_active = True
        self.quiz_score = 0
        self.current_question = 0
        self.display_message("🤖 LearnBot", 
                           "📝 **QUIZ TIME!** 📝\n\n"
                           "Let's test your programming knowledge! I'll ask you 10 questions.\n"
                           "Simply type the number (1-4) of your chosen answer.\n\n"
                           "Good luck! 🍀", "bot")
        self.root.after(2000, self.ask_question)
    
    def ask_question(self):
        if self.current_question < len(self.quiz_questions):
            q = self.quiz_questions[self.current_question]
            question_text = f"**Question {self.current_question + 1}/{len(self.quiz_questions)}:**\n"
            question_text += f"📝 {q['question']}\n\n"
            question_text += "**Your options:**\n"
            
            for i, option in enumerate(q['options']):
                question_text += f"   {i + 1}. {option}\n"
            
            self.display_message("🤖 LearnBot", question_text, "bot")
            self.display_message("🤖 LearnBot", "💭 **Type your answer (1-4):**", "bot")
        else:
            self.end_quiz()
    
    def check_quiz_answer(self, answer):
        try:
            answer_num = int(answer) - 1
            if 0 <= answer_num <= 3:
                q = self.quiz_questions[self.current_question]
                
                if answer_num == q['correct']:
                    self.display_message("🤖 LearnBot", "✅ **Correct!** Well done! 🎉", "success")
                    self.quiz_score += 1
                else:
                    correct_option = q['options'][q['correct']]
                    self.display_message("🤖 LearnBot", f"❌ **Not quite right.** The correct answer is: **{correct_option}**", "error")
                
                if 'explanation' in q:
                    self.display_message("🤖 LearnBot", f"💡 **Explanation:** {q['explanation']}", "bot")
                
                self.current_question += 1
                self.root.after(2500, self.ask_question)
            else:
                self.display_message("🤖 LearnBot", "⚠️ Please enter a number between 1 and 4.", "error")
        except ValueError:
            self.display_message("🤖 LearnBot", "⚠️ Please enter a valid number (1-4).", "error")
    
    def end_quiz(self):
        self.quiz_active = False
        score_percentage = (self.quiz_score / len(self.quiz_questions)) * 100
        
        result_text = f"🏁 **QUIZ COMPLETE!** 🏁\n\n"
        result_text += f"📊 **Your Score:** {self.quiz_score}/{len(self.quiz_questions)} ({score_percentage:.1f}%)\n\n"
        
        if score_percentage >= 90:
            result_text += "🎉 **EXCELLENT WORK!** You're a programming natural! 🌟\n"
            result_text += "Your understanding of programming concepts is impressive!"
        elif score_percentage >= 75:
            result_text += "👍 **GREAT JOB!** You have solid programming knowledge! 💪\n"
            result_text += "Keep building on this strong foundation!"
        elif score_percentage >= 60:
            result_text += "😊 **GOOD PROGRESS!** You're on the right track! 📚\n"
            result_text += "A little more practice and you'll be mastering these concepts!"
        else:
            result_text += "💪 **KEEP GOING!** Every programmer starts somewhere! 🚀\n"
            result_text += "Review the topics and try again - you'll get better each time!"
        
        self.display_message("🤖 LearnBot", result_text, "bot")
        
        self.user_progress['quiz_scores'].append({
            'score': self.quiz_score,
            'total': len(self.quiz_questions),
            'percentage': score_percentage,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    def show_help(self):
        help_text = """
🤖 **LEARNBOT - HELP GUIDE** 🤖

🎯 **QUICK START:**
• Click topic buttons on the left for instant learning
• Type questions naturally like "what are variables?"
• Take quizzes to test your understanding
• Track your progress over time

📚 **LEARNING TOPICS:**

🔹 **Core Programming**
  • Variables & Data Types
  • Loops & Conditionals  
  • Functions & Arrays
  • Algorithms

🔹 **Programming Techniques**
  • Recursion
  • Debugging
  • Pseudocode & Flowcharts

🔹 **Advanced Topics**
  • Data Structures
  • Sorting Algorithms
  • Searching Algorithms

💬 **HOW TO INTERACT:**
• "explain loops" - Learn about loops
• "start quiz" - Begin a knowledge test
• "my progress" - View learning stats
• "help" - Show this guide

🎨 **FEATURES:**
• Clean, friendly interface
• Interactive learning experience
• Progress tracking
• Real-world examples
• Knowledge quizzes

🚀 **TIP:** The best way to learn is by doing! Don't hesitate to ask questions and experiment!
"""
        self.display_message("🤖 LearnBot", help_text, "bot")
    
    def show_progress(self):
        concepts_learned = len(self.user_progress['concepts_learned'])
        total_concepts = len(self.concepts)
        quizzes_taken = len(self.user_progress['quiz_scores'])
        
        progress_text = "📊 **YOUR LEARNING JOURNEY** 📊\n\n"
        
        progress_percentage = (concepts_learned / total_concepts) * 100
        progress_text += f"**Topics Explored:** {concepts_learned}/{total_concepts} ({progress_percentage:.1f}%)\n"
        
        bars = int((concepts_learned / total_concepts) * 20)
        progress_bar = "[" + "█" * bars + "░" * (20 - bars) + "]"
        progress_text += f"**Progress:** {progress_bar}\n\n"
        
        progress_text += f"**Quizzes Completed:** {quizzes_taken}\n"
        
        if quizzes_taken > 0:
            best_score = max([score['percentage'] for score in self.user_progress['quiz_scores']])
            avg_score = sum([score['percentage'] for score in self.user_progress['quiz_scores']]) / quizzes_taken
            progress_text += f"**Best Score:** {best_score:.1f}%\n"
            progress_text += f"**Average Score:** {avg_score:.1f}%\n\n"
        
        if concepts_learned == total_concepts:
            progress_text += "🎉 **OUTSTANDING!** You've explored all available topics! 🌟\n"
            progress_text += "You're building a strong programming foundation!"
        elif progress_percentage >= 70:
            progress_text += "👍 **GREAT PROGRESS!** You're doing amazing! 💪\n"
            progress_text += "Keep exploring the remaining topics!"
        elif progress_percentage >= 40:
            progress_text += "😊 **GOOD MOMENTUM!** You're learning well! 📚\n"
            progress_text += "There's so much more exciting programming knowledge to discover!"
        else:
            progress_text += "🚀 **BEGINNER'S SPIRIT!** Every expert started here! ✨\n"
            progress_text += "Click the topic buttons to start your learning adventure!"
        
        self.display_message("🤖 LearnBot", progress_text, "bot")
    
    def clear_chat(self):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)
        self.display_message("🤖 LearnBot", "🗑️ **Chat cleared!** Ready for more learning! 🚀", "bot")
