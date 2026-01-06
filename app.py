def analyser_texte(texte):
    resultats = []
    texte_lower = texte.lower()
    
    # Détection d'interactions (français + anglais)
    warfarine_keywords = ["warfarin", "warfarine", "coumadin"]
    amoxicilline_keywords = ["amoxicillin", "amoxicilline", "clamoxyl"]
    
    if any(w in texte_lower for w in warfarine_keywords) and any(a in texte_lower for a in amoxicilline_keywords):
        resultats.append("⚠️ INTERACTION: Warfarine + Amoxicilline → Risque hémorragique")
    
    # Contre-indication métformine
    if ("metformin" in texte_lower or "metformine" in texte_lower) and "clairance" in texte_lower:
        # Cherche un nombre entre 20 et 35
        import re
        match = re.search(r'clairance.*?(\d{1,2})\s*(?:ml/min|ml)', texte_lower)
        if match:
            valeur = int(match.group(1))
            if valeur < 30:
                resultats.append(f"🚨 CONTRE-INDICATION: Metformine avec clairance {valeur} ml/min")
    
    # Doublon AINS (français + anglais)
    if (("ibuprofen" in texte_lower or "ibuprofène" in texte_lower) and 
        ("diclofenac" in texte_lower or "diclofénac" in texte_lower)):
        resultats.append("🔴 DOUBLON: Ibuprofène + Diclofénac → Choisir un seul AINS")
    
    return resultats