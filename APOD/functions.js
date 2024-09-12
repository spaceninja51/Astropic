function retrieve_pic() {
    const reponse = fetch("Astropic/data/2024-09-09.json")
    const data = response.json()
    current = data.url
    document.getElementById(today).src=current
}
