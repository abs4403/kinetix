import os
from flask import Flask, render_template, request

app = Flask(__name__)

EXERCISES = [
    {
        "name": "Barbell Squat",
        "body_part": "legs",
        "difficulty": "Intermediate",
        "duration": "45 min",
        "description": "A foundational lower-body lift for building leg strength, power, and overall stability.",
        "demo_url": "https://www.youtube.com/results?search_query=barbell+squat+exercise",
        "focus": "Strength"
    },
    {
        "name": "Romanian Deadlift",
        "body_part": "legs",
        "difficulty": "Intermediate",
        "duration": "40 min",
        "description": "Targets the hamstrings and glutes while improving posterior chain strength and hip mobility.",
        "demo_url": "https://www.youtube.com/results?search_query=romanian+deadlift+exercise",
        "focus": "Strength"
    },
    {
        "name": "Lunges",
        "body_part": "legs",
        "difficulty": "Beginner",
        "duration": "20 min",
        "description": "A unilateral movement that increases balance, leg endurance, and unilateral leg strength.",
        "demo_url": "https://www.youtube.com/results?search_query=lunge+exercise",
        "focus": "Endurance"
    },
    {
        "name": "Bench Press",
        "body_part": "chest",
        "difficulty": "Intermediate",
        "duration": "35 min",
        "description": "A classic upper-body compound move that develops chest, shoulders, and triceps strength.",
        "demo_url": "https://www.youtube.com/results?search_query=bench+press+exercise",
        "focus": "Power"
    },
    {
        "name": "Incline Dumbbell Press",
        "body_part": "chest",
        "difficulty": "Intermediate",
        "duration": "30 min",
        "description": "Targets the upper chest while improving pressing control and shoulder stability.",
        "demo_url": "https://www.youtube.com/results?search_query=incline+dumbbell+press+exercise",
        "focus": "Hypertrophy"
    },
    {
        "name": "Push-Ups",
        "body_part": "chest",
        "difficulty": "Beginner",
        "duration": "15 min",
        "description": "An all-time bodyweight chest and triceps movement that builds upper-body control.",
        "demo_url": "https://www.youtube.com/results?search_query=pushup+exercise",
        "focus": "Endurance"
    },
    {
        "name": "Deadlift",
        "body_part": "back",
        "difficulty": "Advanced",
        "duration": "50 min",
        "description": "A full-body lift focusing on posterior chain strength, posture, and resilience.",
        "demo_url": "https://www.youtube.com/results?search_query=deadlift+exercise",
        "focus": "Strength"
    },
    {
        "name": "Pull-Up",
        "body_part": "back",
        "difficulty": "Intermediate",
        "duration": "30 min",
        "description": "Build a stronger upper back, biceps, and core with this demanding bodyweight exercise.",
        "demo_url": "https://www.youtube.com/results?search_query=pull+up+exercise",
        "focus": "Endurance"
    },
    {
        "name": "Bent-Over Row",
        "body_part": "back",
        "difficulty": "Intermediate",
        "duration": "25 min",
        "description": "A back-building staple that strengthens the upper back and improves posture.",
        "demo_url": "https://www.youtube.com/results?search_query=bent+over+row+exercise",
        "focus": "Strength"
    },
    {
        "name": "Shoulder Press",
        "body_part": "shoulders",
        "difficulty": "Intermediate",
        "duration": "25 min",
        "description": "Develop strong, stable shoulders with controlled overhead pressing patterns.",
        "demo_url": "https://www.youtube.com/results?search_query=shoulder+press+exercise",
        "focus": "Strength"
    },
    {
        "name": "Lateral Raise",
        "body_part": "shoulders",
        "difficulty": "Beginner",
        "duration": "18 min",
        "description": "Isolates the medial delts to improve shoulder width and arm definition.",
        "demo_url": "https://www.youtube.com/results?search_query=lateral+raise+exercise",
        "focus": "Tone"
    },
    {
        "name": "Front Raise",
        "body_part": "shoulders",
        "difficulty": "Beginner",
        "duration": "15 min",
        "description": "A focused shoulder-builder that strengthens the front delts and improve overhead control.",
        "demo_url": "https://www.youtube.com/results?search_query=front+raise+exercise",
        "focus": "Tone"
    },
    {
        "name": "Russian Twist",
        "body_part": "core",
        "difficulty": "Beginner",
        "duration": "15 min",
        "description": "An effective core move for building rotational power and increasing trunk control.",
        "demo_url": "https://www.youtube.com/results?search_query=russian+twist+exercise",
        "focus": "Core"
    },
    {
        "name": "Plank",
        "body_part": "core",
        "difficulty": "Beginner",
        "duration": "10 min",
        "description": "Build anti-extension strength and core stability that supports good posture and movement quality.",
        "demo_url": "https://www.youtube.com/results?search_query=plank+exercise",
        "focus": "Stability"
    },
    {
        "name": "Hanging Knee Raise",
        "body_part": "core",
        "difficulty": "Intermediate",
        "duration": "20 min",
        "description": "A challenging abdominal movement that targets the lower abs and hip flexors.",
        "demo_url": "https://www.youtube.com/results?search_query=hanging+knee+raise+exercise",
        "focus": "Strength"
    },
    {
        "name": "Dumbbell Curl",
        "body_part": "arms",
        "difficulty": "Beginner",
        "duration": "20 min",
        "description": "Target your biceps with a controlled, high-rep arm workout that builds definition.",
        "demo_url": "https://www.youtube.com/results?search_query=dumbbell+curl+exercise",
        "focus": "Tone"
    },
    {
        "name": "Triceps Dip",
        "body_part": "arms",
        "difficulty": "Intermediate",
        "duration": "15 min",
        "description": "Build triceps strength with a bodyweight movement that also challenges the shoulders.",
        "demo_url": "https://www.youtube.com/results?search_query=triceps+dip+exercise",
        "focus": "Strength"
    },
    {
        "name": "Hammer Curl",
        "body_part": "arms",
        "difficulty": "Beginner",
        "duration": "18 min",
        "description": "Develop forearm and biceps strength while improving grip and elbow stability.",
        "demo_url": "https://www.youtube.com/results?search_query=hammer+curl+exercise",
        "focus": "Power"
    },
    {
        "name": "Hip Thrust",
        "body_part": "glutes",
        "difficulty": "Intermediate",
        "duration": "30 min",
        "description": "Activate the glutes and improve lower-body power with this targeted posterior chain move.",
        "demo_url": "https://www.youtube.com/results?search_query=hip+thrust+exercise",
        "focus": "Power"
    },
    {
        "name": "Glute Bridge",
        "body_part": "glutes",
        "difficulty": "Beginner",
        "duration": "12 min",
        "description": "A simple but highly effective glute activation drill that supports hip strength and posture.",
        "demo_url": "https://www.youtube.com/results?search_query=glute+bridge+exercise",
        "focus": "Activation"
    },
    {
        "name": "Single-Leg Romanian Deadlift",
        "body_part": "glutes",
        "difficulty": "Advanced",
        "duration": "25 min",
        "description": "Improve unilateral strength, balance, and hamstring control while targeting the glutes.",
        "demo_url": "https://www.youtube.com/results?search_query=single+leg+romanian+deadlift+exercise",
        "focus": "Balance"
    }
]

YOGA_POSES = [
    {
        "name": "Sun Salutation",
        "focus": "flexibility",
        "difficulty": "Beginner",
        "duration": "15 min",
        "description": "A flowing routine that wakes up the body, improves mobility, and energizes the mind.",
        "demo_url": "https://www.youtube.com/results?search_query=sun+salutation+yoga",
    },
    {
        "name": "Warrior II",
        "focus": "strength",
        "difficulty": "Intermediate",
        "duration": "12 min",
        "description": "Build lower-body strength, balance, and focus while opening your hips and chest.",
        "demo_url": "https://www.youtube.com/results?search_query=warrior+ii+yoga+pose",
    },
    {
        "name": "Tree Pose",
        "focus": "balance",
        "difficulty": "Beginner",
        "duration": "8 min",
        "description": "Improve stability and concentration with this grounding balance pose for the hips and legs.",
        "demo_url": "https://www.youtube.com/results?search_query=tree+pose+yoga",
    },
    {
        "name": "Child's Pose",
        "focus": "relaxation",
        "difficulty": "Beginner",
        "duration": "10 min",
        "description": "A restorative stretch that releases tension in the back, hips, and shoulders.",
        "demo_url": "https://www.youtube.com/results?search_query=childs+pose+yoga",
    },
    {
        "name": "Downward Dog",
        "focus": "flexibility",
        "difficulty": "Intermediate",
        "duration": "10 min",
        "description": "Lengthen the hamstrings and calves while enhancing posture and full-body mobility.",
        "demo_url": "https://www.youtube.com/results?search_query=downward+dog+yoga",
    },
    {
        "name": "Boat Pose",
        "focus": "strength",
        "difficulty": "Intermediate",
        "duration": "12 min",
        "description": "Strengthen the core and hip flexors with this steady, controlled seated balance pose.",
        "demo_url": "https://www.youtube.com/results?search_query=boat+pose+yoga",
    },
    {
        "name": "Crescent Lunge",
        "focus": "strength",
        "difficulty": "Intermediate",
        "duration": "15 min",
        "description": "Open the hips and thighs while building strength through a stable, grounded lunge shape.",
        "demo_url": "https://www.youtube.com/results?search_query=crescent+lunge+yoga",
    },
    {
        "name": "Pigeon Pose",
        "focus": "flexibility",
        "difficulty": "Intermediate",
        "duration": "14 min",
        "description": "A deep hip opener that releases tightness in the glutes, hips, and lower back.",
        "demo_url": "https://www.youtube.com/results?search_query=pigeon+pose+yoga",
    },
    {
        "name": "Cat-Cow",
        "focus": "mobility",
        "difficulty": "Beginner",
        "duration": "8 min",
        "description": "Warm up the spine and improve mobility with slow, controlled movements between flexion and extension.",
        "demo_url": "https://www.youtube.com/results?search_query=cat+cow+yoga",
    },
    {
        "name": "Seated Forward Fold",
        "focus": "flexibility",
        "difficulty": "Beginner",
        "duration": "10 min",
        "description": "A calming hamstring stretch that helps release tension in the lower back and legs.",
        "demo_url": "https://www.youtube.com/results?search_query=seated+forward+fold+yoga",
    },
    {
        "name": "Corpse Pose",
        "focus": "relaxation",
        "difficulty": "Beginner",
        "duration": "12 min",
        "description": "A deeply restorative pose for releasing stress, calming the nervous system, and resetting after training.",
        "demo_url": "https://www.youtube.com/results?search_query=corpse+pose+yoga",
    },
    {
        "name": "Garland Pose",
        "focus": "mobility",
        "difficulty": "Intermediate",
        "duration": "11 min",
        "description": "This squat-based pose improves lower-body mobility, flexibility, and balance.",
        "demo_url": "https://www.youtube.com/results?search_query=garland+pose+yoga",
    }
]

BODY_PARTS = ["all", "chest", "back", "legs", "shoulders", "core", "arms", "glutes"]
YOGA_FOCUSES = ["all", "flexibility", "strength", "balance", "mobility", "relaxation"]
ACTIVITY_LEVELS = {
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "active": 1.725,
    "very_active": 1.9
}


@app.route("/")
def index():
    return render_template(
        "index.html",
        featured_exercises=EXERCISES[:3],
        featured_poses=YOGA_POSES[:3]
    )


@app.route("/exercises")
def exercises():
    selected_part = request.args.get("part", "all")
    filtered = EXERCISES if selected_part == "all" else [
        item for item in EXERCISES if item["body_part"] == selected_part
    ]
    return render_template(
        "exercises.html",
        exercises=filtered,
        selected_part=selected_part,
        body_parts=BODY_PARTS
    )


@app.route("/yoga")
def yoga():
    selected_focus = request.args.get("focus", "all")
    filtered = YOGA_POSES if selected_focus == "all" else [
        item for item in YOGA_POSES if item["focus"] == selected_focus
    ]
    return render_template(
        "yoga.html",
        poses=filtered,
        selected_focus=selected_focus,
        yoga_focuses=YOGA_FOCUSES
    )


@app.route("/calories")
def calories():
    result = None
    if request.args.get("weight"):
        try:
            weight = float(request.args.get("weight", 0))
            height = float(request.args.get("height", 0))
            age = float(request.args.get("age", 0))
            sex = request.args.get("sex", "male")
            activity = request.args.get("activity", "moderate")
            duration = float(request.args.get("duration", 30))
            goal = request.args.get("goal", "maintain")
            if sex == "female":
                bmr = 10 * weight + 6.25 * height - 5 * age - 161
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            maintenance = bmr * ACTIVITY_LEVELS.get(activity, 1.55)
            target = maintenance - 300 if goal == "lose" else maintenance + 250 if goal == "gain" else maintenance
            burned = maintenance * (duration / 60) * 0.4
            result = {
                "maintenance": round(maintenance),
                "target": round(target),
                "burned": round(burned),
                "goal": goal
            }
        except ValueError:
            result = None
    return render_template("calories.html", result=result)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/health")
def health():
    return {"status": "ok", "app": "kinetix"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
