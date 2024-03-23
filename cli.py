import argparse
from perplexity import Chat, Search

def main():
    class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter,
                      argparse.RawDescriptionHelpFormatter):
        pass
    parser = argparse.ArgumentParser(
        description="""
    ------------------------------------------------------------------
                          Perplexity AI Toolkit                                 
                   API Wrapper & Command-line Interface               
                          [v1.2.0] by @rmncldyo                      
    ------------------------------------------------------------------

    Perplexity AI toolit is an API wrapper and command-line interface for the suite of large-language models offered by Perplexity Labs.

    | Option(s)                | Description                                   | Example Usage                                                                 |
    |--------------------------|-----------------------------------------------|-------------------------------------------------------------------------------|
    | -c,  --chat              | Enable chat mode                              | --chat                                                                        |
    | -s,  --search            | Enable search mode                            | --search                                                                      |
    | -p,  --prompt            | Initial user prompt                           | --prompt "How are you doing today my ai friend?"                              |
    | -q,  --query             | Search query                                  | --query "What is today's date?"                                               |
    | -a,  --api_key           | Perplexity API key for authentication         | --api_key "api_key_goes_here"                                                 |
    | -m,  --model             | The model you would like to use               | --model "model_name_goes_here"                                                |
    | -sp, --system_prompt     | System prompt                                 | --system_prompt "You are an advanced ai assistant."                           |
    | -st, --stream            | Enable streaming mode for responses           | --stream                                                                      |
    | -mt, --max_tokens        | Maximum number of tokens to generate          | --max_tokens 1024                                                             |
    | -tm, --temperature       | Sampling temperature                          | --temperature 0.7                                                             |
    | -tp, --top_p             | Nucleus sampling threshold                    | --top_p 0.9                                                                   |
    | -tk, --top_k             | Top-k sampling threshold                      | --top_k 40                                                                    |
    | -pp, --presence_penalty  | Penalize new tokens based on their presence.  | --presence_penalty 0.5                                                        |
    | -fp, --frequency_penalty | Penalize new tokens based on their frequency. | --frequency_penalty 0.5                                                       |
    """,
        formatter_class=CustomFormatter,
        epilog="For detailed usage information, visit our ReadMe here: github.com/RMNCLDYO/perplexity-ai-toolkit"
    )
    parser.add_argument('-c', '--chat', action='store_true', help='Enable chat mode')
    parser.add_argument('-s', '--search', action='store_true', help='Enable search mode')
    parser.add_argument('-p', '--prompt', type=str, help='Initial user prompt')
    parser.add_argument('-q', '--query', type=str, help='Search query')
    parser.add_argument('-a', '--api_key', type=str, help='Perplexity API key for authentication')
    parser.add_argument('-m', '--model', type=str, help='The model you would like to use')
    parser.add_argument('-sp', '--system_prompt', type=str, help='System prompt')
    parser.add_argument('-st', '--stream', action='store_true', help='Enable streaming mode for responses')
    parser.add_argument('-mt', '--max_tokens', type=int, help='Maximum number of tokens to generate')
    parser.add_argument('-tm', '--temperature', type=float, help='Sampling temperature')
    parser.add_argument('-tp', '--top_p', type=float, help='Nucleus sampling threshold')
    parser.add_argument('-tk', '--top_k', type=int, help='Top-k sampling threshold')
    parser.add_argument('-pp', '--presence_penalty', type=float, help='Penalize new tokens based on their presence.')
    parser.add_argument('-fp', '--frequency_penalty', type=float, help='Penalize new tokens based on their frequency.')

    args = parser.parse_args()
    
    if args.chat:
        Chat().run(args.api_key, args.model, args.prompt, args.system_prompt, args.stream, args.max_tokens, args.temperature, args.top_p, args.top_k, args.presence_penalty, args.frequency_penalty)
    elif args.search:
        Search().run(args.api_key, args.model, args.query, args.system_prompt, args.stream, args.max_tokens, args.temperature, args.top_p, args.top_k, args.presence_penalty, args.frequency_penalty)
    else:
        print("Error: Please specify a mode to use. Use --help for more information.")
        exit()

if __name__ == "__main__":
    main()