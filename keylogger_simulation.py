import time


def security_demo():
    print("=" * 55)
    print("          KEYLOGGER SECURITY RESEARCH DEMO")
    print("=" * 55)

    print("\nThis is an educational keylogger simulation.")
    print("It does NOT capture real keyboard input.")
    print("It only demonstrates how keystroke logging could")
    print("appear in a security research environment.")

    print("\nSimulated Keystrokes")
    print("-" * 55)

    simulated_keys = [
        "H",
        "e",
        "l",
        "l",
        "o",
        " ",
        "W",
        "o",
        "r",
        "l",
        "d"
    ]

    logged_keys = []

    for key in simulated_keys:
        logged_keys.append(key)
        print("Detected key:", repr(key))
        time.sleep(0.1)

    print("\n" + "-" * 55)

    simulated_text = "".join(logged_keys)

    print("Simulated captured text:", simulated_text)

    print("\nSecurity Risks")
    print("-" * 55)
    print("- Keystrokes can potentially expose sensitive information.")
    print("- Passwords and private messages can be targeted by malware.")
    print("- Unauthorized keylogging can violate privacy and security.")

    print("\nSecurity Recommendations")
    print("-" * 55)
    print("- Keep operating systems and applications updated.")
    print("- Use reputable security software.")
    print("- Avoid installing unknown applications.")
    print("- Use multi-factor authentication where available.")
    print("- Never run unknown scripts with unnecessary privileges.")

    print("\n" + "=" * 55)
    print("Security research demonstration completed.")
    print("=" * 55)


security_demo()
