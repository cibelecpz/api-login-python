const botao = document.querySelector("button");

botao.addEventListener("click", async function () {
    const email = document.querySelector("#email").value;
    const senha = document.querySelector("#senha").value;

    const resposta = await fetch("http://127.0.0.1:8000/login?email=" + email + "&senha=" + senha, {
        method: "POST"
    });

    const dados = await resposta.json();

    if (dados.mensagem) {
    window.location.href = "home.html";
} else {
    alert(dados.erro);
}
});