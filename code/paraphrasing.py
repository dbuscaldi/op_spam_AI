import os, random
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

device = "cpu"

tokenizer = AutoTokenizer.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")

model = AutoModelForSeq2SeqLM.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base").to(device)

def paraphrase(
    question,
    num_beams=5,
    num_beam_groups=5,
    num_return_sequences=5,
    repetition_penalty=10.0,
    diversity_penalty=3.0,
    no_repeat_ngram_size=2,
    temperature=0.9,
    max_length=256
):
    input_ids = tokenizer(
        f'paraphrase: {question}',
        return_tensors="pt", padding="longest",
        max_length=max_length,
        truncation=True,
    ).input_ids

    outputs = model.generate(
        input_ids, temperature=temperature, repetition_penalty=repetition_penalty,
        num_return_sequences=num_return_sequences, no_repeat_ngram_size=no_repeat_ngram_size,
        num_beams=num_beams, num_beam_groups=num_beam_groups,
        max_length=max_length, diversity_penalty=diversity_penalty
    )

    res = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return res

def find_txt_files(directory):
    txt_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt') and 'deceptive' not in root:
                txt_files.append(os.path.join(root, file))

    return txt_files

def generate_reviews(examples, review_type):
    generated_reviews = []
    output_directory = "paraphrased_{}".format(review_type)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for example in examples:
        paraphrased_text = random.choice(paraphrase(example[1])) #randomly select one out of 5 reviews
        output_file = os.path.join(output_directory, example[0])
        with open(output_file, 'w', encoding='utf-8') as file:
                file.write("{}".format(paraphrased_text))

# Replace 'path/to/your/directory' with the actual path to the directory you want to search in.
d1 = 'generated_GPT3_positive'
d2 = 'generated_GPT3_negative'

pos_texts = []
for txt_file in find_txt_files(d1):
    print(txt_file)
    with open(txt_file, 'r') as file:
        text = file.read()
        fname = os.path.basename(txt_file)
        pos_texts.append((fname,text))

neg_texts = []
for txt_file in find_txt_files(d2):
    print(txt_file)
    with open(txt_file, 'r') as file:
        text = file.read()
        fname = os.path.basename(txt_file)
        neg_texts.append((fname,text))

print("generating paraphrases...")
generate_reviews(pos_texts, "positive")
print("positives done.")

generate_reviews(neg_texts, "negative")
print("negatives done.")
print("finished.")

#text = gen_texts[0]
#print(text)
#print(paraphrase(text))
