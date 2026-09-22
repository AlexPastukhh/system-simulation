from system_simulation.curriculum.finance.ch01 import FinancialClaimsScenario


def main() -> None:
    scenario = FinancialClaimsScenario()
    scenario.run_complete(100)
    for frame in scenario.trace.frames:
        print(f"\nSTEP {frame.step}: {frame.event}")
        print(frame.description)
        if not frame.changes:
            print("  no state changes")
        for change in frame.changes:
            print(f"  {change.path}: {change.before} -> {change.after}")


if __name__ == "__main__":
    main()
