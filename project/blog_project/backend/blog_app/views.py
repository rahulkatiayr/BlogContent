from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# In-memory storage (instead of a database)
tasks = [
    {
        "id": 1,
        "title": "The Rise of Artificial Intelligence",
        "content": "Artificial Intelligence (AI) has transformed industries, from healthcare to finance. With advancements in deep learning and neural networks, AI systems can now perform complex tasks with human-like efficiency. However, ethical concerns regarding data privacy and job displacement continue to be debated. The future of AI is promising, with applications in automation, personalized experiences, and even creative fields like music and art.",
        "likes": 250,
        "comments": [
            {"user": "Alice", "comment": "AI is changing the world!"},
            {"user": "Bob", "comment": "I’m excited but also worried about AI ethics."}
        ]
    },
    {
        "id": 2,
        "title": "The Future of Cybersecurity",
        "content": "As cyber threats evolve, so do security measures. With an increasing number of cyberattacks targeting businesses and individuals, cybersecurity has become more crucial than ever. The rise of quantum computing poses both risks and opportunities for encryption methods. Organizations must adopt zero-trust security models and AI-driven threat detection to stay ahead of attackers.",
        "likes": 180,
        "comments": [
            {"user": "Charlie", "comment": "Cybersecurity is the need of the hour!"},
            {"user": "Dave", "comment": "Zero-trust architecture is a game changer."}
        ]
    },
    {
        "id": 3,
        "title": "Blockchain Beyond Cryptocurrency",
        "content": "While blockchain technology is widely known for powering cryptocurrencies like Bitcoin and Ethereum, its applications extend far beyond digital currency. Industries such as supply chain management, healthcare, and real estate are leveraging blockchain for transparent and secure transactions. Smart contracts are automating agreements without the need for intermediaries, reducing costs and increasing efficiency.",
        "likes": 220,
        "comments": [
            {"user": "Eve", "comment": "Smart contracts are the future!"},
            {"user": "Frank", "comment": "Blockchain has so much potential beyond crypto."}
        ]
    },
    {
        "id": 4,
        "title": "Space Exploration: The Next Frontier",
        "content": "With missions planned for Mars and beyond, space exploration is reaching new heights. Private companies like SpaceX and Blue Origin are pushing boundaries with reusable rockets and ambitious colonization plans. NASA’s Artemis program aims to return humans to the Moon, paving the way for deep-space exploration. The possibility of interplanetary travel is no longer a dream but a work in progress.",
        "likes": 300,
        "comments": [
            {"user": "Grace", "comment": "I hope we see humans on Mars soon!"},
            {"user": "Hank", "comment": "Space travel fascinates me!"}
        ]
    },
    {
        "id": 5,
        "title": "Understanding the Internet of Things (IoT)",
        "content": "The Internet of Things (IoT) refers to the growing network of interconnected devices that communicate and share data. From smart homes to industrial automation, IoT is revolutionizing daily life. However, security concerns arise as more devices become connected, making them potential targets for cyberattacks. Ensuring strong encryption and regular software updates is critical in securing IoT networks.",
        "likes": 140,
        "comments": [
            {"user": "Ivy", "comment": "IoT makes life easier, but security is a big issue."},
            {"user": "Jack", "comment": "Can’t wait for more smart home innovations!"}
        ]
    },
    {
        "id": 6,
        "title": "Machine Learning: Applications and Challenges",
        "content": "Machine learning has powered innovations in healthcare, finance, and marketing. From medical diagnosis to predictive analytics, ML models analyze vast amounts of data to find patterns and make accurate predictions. However, issues such as biased algorithms and data privacy remain challenges that need to be addressed. Responsible AI development is key to making ML beneficial for everyone.",
        "likes": 190,
        "comments": [
            {"user": "Kelly", "comment": "ML is revolutionizing every industry!"},
            {"user": "Leo", "comment": "We need more transparency in AI decision-making."}
        ]
    },
    {
        "id": 7,
        "title": "The Role of Quantum Computing in the Future",
        "content": "Quantum computing has the potential to solve problems that traditional computers cannot. By leveraging the principles of quantum mechanics, quantum computers can perform calculations at unprecedented speeds. Fields like cryptography, materials science, and drug discovery are expected to benefit significantly. However, challenges such as hardware limitations and error rates need to be overcome before mainstream adoption.",
        "likes": 170,
        "comments": [
            {"user": "Mia", "comment": "Quantum computing is mind-blowing!"},
            {"user": "Noah", "comment": "This could change cybersecurity forever!"}
        ]
    },
    {
        "id": 8,
        "title": "The Evolution of Web Development",
        "content": "Web development has come a long way from static HTML pages to dynamic, full-stack applications. JavaScript frameworks like React, Vue, and Angular dominate the frontend, while backend technologies like Node.js, Django, and Flask provide robust server-side functionality. The rise of Progressive Web Apps (PWAs) is blurring the lines between web and mobile applications, offering seamless user experiences.",
        "likes": 200,
        "comments": [
            {"user": "Olivia", "comment": "React is my favorite framework!"},
            {"user": "Peter", "comment": "PWAs are the future of web apps."}
        ]
    },
    {
        "id": 9,
        "title": "5G Technology and Its Impact",
        "content": "The rollout of 5G networks is revolutionizing mobile connectivity. With ultra-fast speeds and low latency, 5G enables new applications in augmented reality, IoT, and smart cities. However, concerns about infrastructure costs and health effects remain topics of debate. As countries compete to lead in 5G deployment, the technology is expected to reshape industries worldwide.",
        "likes": 130,
        "comments": [
            {"user": "Quinn", "comment": "5G will enable so many new innovations!"},
            {"user": "Ryan", "comment": "Hope the network coverage expands soon!"}
        ]
    },
    {
        "id": 10,
        "title": "Cloud Computing: The Backbone of Digital Transformation",
        "content": "Cloud computing has become essential for businesses and individuals alike. Services like AWS, Google Cloud, and Microsoft Azure provide scalable and cost-effective solutions for storage, computing, and AI services. The shift to cloud-native applications is accelerating, but challenges such as data security and vendor lock-in need to be carefully managed to ensure long-term benefits.",
        "likes": 240,
        "comments": [
            {"user": "Sophia", "comment": "Cloud computing makes everything so much easier!"},
            {"user": "Tom", "comment": "Security in the cloud is still a big concern for me."}
        ]
    }
]


@api_view(['GET'])
def get_posts(request):
    """Return all blog posts"""
    return Response(tasks)

@api_view(['POST'])
def add_post(request):
    """Add a new blog post"""
    data = request.data
    new_post = {
        "id": len(tasks) + 1,  # Auto-increment ID
        "title": data.get('title'),
        "content": data.get('content')
    }
    tasks.append(new_post)
    return Response(new_post, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_post_by_id(request, post_id):
    """Return a single post by ID"""
    post = next((task for task in tasks if task["id"] == post_id), None)
    if post:
        return Response(post)
    return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
