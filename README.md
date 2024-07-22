# Information Gathering Tool

This Python script serves as an information gathering tool that collects various details about a given domain or IP address. It utilizes several libraries and APIs for retrieving domain information, DNS records, and Shodan search results.

## Dependencies

Ensure you have the following Python libraries installed:
- `whois`
- `dnspython`
- `requests`
- `shodan`
- `colorama`

You can install these dependencies using pip:
```bash
pip install whois dnspython requests shodan colorama
git clone https://github.com/your_username/your_repository.git
cd your_repository
python3 information_gathering.py -d example.com -i <optional_target_ip> -o <optional_output_file>


