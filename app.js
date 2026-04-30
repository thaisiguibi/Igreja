const API = https://api-igreja-xfmj.onrender.com

// ===== UI =====
function show(msg) {
    document.getElementById("msg").innerText = msg
}

// ===== TOKEN =====
function getToken() {
    return localStorage.getItem("token")
}

function authHeaders() {
    const token = getToken()

    if (!token) {
        show("Faça login primeiro")
        throw new Error("Sem token")
    }

    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
}

// ===== LOGIN =====
async function login() {
    const res = await fetch(API + "/users/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: document.getElementById("name").value,
            password: document.getElementById("password").value
        })
    })

    const data = await res.json()
    console.log(data)

    const token = data.data?.access_token || data.access_token

    if (token) {
        localStorage.setItem("token", token)
        show("Login OK")
    } else {
        show("Erro no login")
    }
}

// ===== CREATE POST =====
async function createPost() {
    try {
        const res = await fetch(API + "/posts/", {
            method: "POST",
            headers: authHeaders(),
            body: JSON.stringify({
                title: document.getElementById("title").value,
                content: document.getElementById("content").value
            })
        })

        const data = await res.json()
        console.log(data)

        if (data.data) {
            show("Post criado")
            loadPosts()
        } else {
            show("Erro ao criar post")
        }

    } catch (err) {
        show("Erro: " + err)
    }
}

// ===== LIST POSTS =====
async function loadPosts() {
    const res = await fetch("http://localhost:8000/posts/")
    const data = await res.json()

    console.log("DATA:", data)

    const list = document.getElementById("posts")
    list.innerHTML = ""

    const posts = data.data?.itens || []

    posts.forEach(p => {
        const li = document.createElement("li")

        // ✅ agora é objeto
        li.innerText = p.title + " - " + p.content

        list.appendChild(li)
    })
}

// ===== SUBSCRIBE =====
async function subscribe() {
    const email = document.getElementById("email").value

    // validação vem aqui
    if (!email.includes("@")) {
        show("Email inválido")
        return
    }

    // só executa se passou na validação
    const res = await fetch(API + "/newsletter/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email })
    })

    const data = await res.json()

    if (data.data) {
        show("Inscrito com sucesso")
    } else {
        show(data.message || "Erro")
    }
}
