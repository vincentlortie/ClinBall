import json

def maf_calculator(allele_annotations):
    if len(allele_annotations) == 0:
        return
    frequencies = allele_annotations[0]["frequency"]
    if len(frequencies) == 0:
        return
    return 1 - frequencies[0]["allele_count"]/frequencies[0]["total_count"]

my_file = []
count = 0
with open('refsnp-other.json') as f:
    for line in f:
        count += 1
        j = json.loads(line)
        maf = maf_calculator(j["primary_snapshot_data"]["allele_annotations"])
        d = {
            "id": j["refsnp_id"],
            "type": j["primary_snapshot_data"]["variant_type"],
            "maf": maf,
            "citations": len(j["citations"])
            # TODO: available in the vcf file
            # "function_conseq":
        }
        my_file.append(d)
        if count == 1000:
            break

with open('basic_dbsnp.json', "w") as write_file:
    json.dump(my_file, write_file)
