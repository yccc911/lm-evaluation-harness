import datasets

def doc_to_text(item):
    # {'question': '下列選項中哪個讀音與「宜」相同？', 'options': ['棨', '縏', '葞', '飴'], 'pronounciations': ['ㄑㄧˇ', 'ㄆㄢˊ', 'ㄇㄧˇ', 'ㄧˊ'], 'label': 3}
    prompt = f"{item['question']}\nA. {item['A']}\nB. {item['B']}\nC. {item['C']}\nD. {item['D']}\nAnswer:"
    return prompt

def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    def _helper(doc):
        # modifies the contents of a single
        # document in our dataset.
        answer_list = ["A", "B", "C", "D"]
        choices = [doc["A"], doc["B"], doc["C"], doc["D"]]
        out_doc = {
            "questions": doc["question"],
            "choices": choices,
            "goal": doc["label"],
        }
        return out_doc

    return dataset.map(_helper)  # returns back a datasets.Dataset object