async function carregarProdutos() {
    const resposta = await fetch("http://127.0.0.1:8000/produtos");

    const produtos = await resposta.json();

    const lista = document.querySelector("#lista-produtos");

    produtos.forEach(function (produto) {
        lista.innerHTML += `
            <div class="produto">
    <h2>📦 ${produto.nome}</h2>
    <p>💰 R$ ${produto.preco}</p>

    <button onclick="comprar('${produto.nome}')">
🛒 Comprar
</button>
    <button>✏️ Editar</button>
    <button>🗑️ Excluir</button>
</div>
        `;
    });
}

carregarProdutos();
function comprar(nome) {
    alert("🛒 Você comprou: " + nome);
}