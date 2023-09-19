def create_system_message(config):
    wc = int(config["DEFAULT"]["MAX_WORD_COUNT"])
    sc = int(config["DEFAULT"]["MAX_SENTENCE_COUNT"])
    if sc > 1:
        sc = f"{sc-1} - {sc}"

    message = [{
        "role": "system",
        "content": f"""I will provide you with piece of content (e.g. articles, papers, documentation, etc.)

        You will generate increasingly concise, entity-dense summaries of the content.

        Repeat the following 2 steps 5 times.

        Step 1. Identify 1-3 informative Entities (";" delimited) from the Article which are missing from the previously generated summary.

        Step 2. Write a new, denser summary of identical length which covers every entity and detail from the previous summary plus the Missing Entities.

        A Missing Entity is:

        Relevant: to the main story.
        Specific: descriptive yet concise (5 words or fewer).
        Novel: not in the previous summary.
        Faithful: present in the content piece.
        Anywhere: located anywhere in the Article.

        Guidelines:

        The first summary should be long ({sc} sentences, -{wc} words) yet highly non-specific, containing little information beyond the entities marked as missing. Use overly verbose language and fillers (e.g., "this article discusses") to reach -{wc} words.
        Make every word count: re-write the previous summary to improve flow and make space for additional entities.
        Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
        The summaries should become highly dense and concise yet self-contained, e.g., easily understood without the Article.
        Missing entities can appear anywhere in the new summary.
        Never drop entities from the previous summary. If space cannot be made, add fewer new entities.
        Remember, use the exact same number of words for each summary.
        Answer in JSON. The JSON should be a list (length 5) of dictionaries whose keys are "Missing_Entities" and "Denser_Summary"."""}]
    return message