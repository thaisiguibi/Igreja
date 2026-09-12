const API = "https://api-igreja-xfmj.onrender.com"

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
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: document.getElementById("name").value,
            password: document.getElementById("password").value
        })
    })

    const data = await res.json()

    if (res.ok) {
        localStorage.setItem("token", data.access_token)
        show("Login realizado")
    } else {
        show(data.message || "Erro ao fazer login")
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

        if (res.ok) {
            show("Post criado")
            loadPosts()
        } else {
            show(data.message || "Erro ao criar post")
        }

    } catch (err) {
        show("Erro: " + err)
    }
}


// ===== SUBSCRIBE =====

async function subscribe() {
    const email = document.getElementById("email").value

    if (!email.includes("@")) {
        show("Email inválido")
        return
    }

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


// ===== LIST POSTS =====

async function loadPosts() {
    const res = await fetch(API + "/posts/")
    const data = await res.json()

    console.log("DATA:", data)

    const list = document.getElementById("posts")

    if (!list) {
        return
    }

    list.innerHTML = ""

    const posts = data.items || []

    posts.forEach(post => {
        const artigo = document.createElement("article")

        artigo.innerHTML = `
            <h2>${post.title}</h2>
            <p>${post.content}</p>
            <small>Publicado por: ${post.user.name}</small>
        `

        list.appendChild(artigo)
    })
}

loadPosts()
