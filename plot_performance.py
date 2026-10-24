"""
======================================================================
PLANT DISEASE DETECTION - PERFORMANCE GRAPH GENERATOR
======================================================================
File Name : plot_performance.py
Location  : Place directly in the project root folder:
            c:\\Users\\balla\\Domain_project\\Plant_Disease_Detection\\plot_performance.py

Description:
Reads the training log (reports/training_log.csv) and generates
publication-quality performance charts:
  1. Accuracy Curve (Training vs. Validation Accuracy)
  2. Loss Curve (Categorical Cross-Entropy Loss)
  3. Combined Dashboard (Accuracy & Loss Side-by-Side)

Outputs are saved in the 'reports/' directory and displayed on screen.
======================================================================
"""

import csv
import os
from pathlib import Path
import matplotlib.pyplot as plt

# --------------------------------------------------------------------
# 1. PATH CONFIGURATION
# --------------------------------------------------------------------
PROJECT_DIR = Path(__file__).resolve().parent
REPORTS_DIR = PROJECT_DIR / "reports"
LOG_CSV_PATH = REPORTS_DIR / "training_log.csv"

# Ensure reports directory exists
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def load_training_data(csv_path):
    """
    Parses the training log CSV safely, handling dynamic column widths
    from multi-phase transfer learning and fine-tuning.
    """
    if not csv_path.exists():
        raise FileNotFoundError(f"Training log file not found at: {csv_path}")

    epochs = []
    train_acc = []
    val_acc = []
    train_loss = []
    val_loss = []

    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or not row[0].strip() or row[0].strip().lower() == "epoch":
                continue
            try:
                ep = int(row[0])
                acc = float(row[1]) * 100
                loss = float(row[3])

                if len(row) == 6:
                    v_acc = float(row[4]) * 100
                    v_loss = float(row[5])
                elif len(row) >= 8:
                    v_acc = float(row[5]) * 100
                    v_loss = float(row[6])
                else:
                    continue

                epochs.append(ep + 1)
                train_acc.append(acc)
                val_acc.append(v_acc)
                train_loss.append(loss)
                val_loss.append(v_loss)
            except (ValueError, IndexError):
                continue

    return epochs, train_acc, val_acc, train_loss, val_loss


def generate_performance_graphs():
    print("=" * 70)
    print("GENERATING MODEL PERFORMANCE GRAPHS")
    print("=" * 70)

    epochs, train_acc, val_acc, train_loss, val_loss = load_training_data(LOG_CSV_PATH)
    print(f"Loaded {len(epochs)} training epochs successfully.")

    best_val_idx = val_acc.index(max(val_acc))
    best_epoch = epochs[best_val_idx]
    best_val_acc = val_acc[best_val_idx]
    final_val_acc = val_acc[-1]

    # Visual styling
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    # ================================================================
    # 1. ACCURACY CURVE
    # ================================================================
    plt.figure(figsize=(9, 5.5), dpi=300)
    plt.plot(epochs, train_acc, label="Training Accuracy", color="#1E88E5", linewidth=2.2)
    plt.plot(epochs, val_acc, label="Validation Accuracy", color="#D81B60", linewidth=2.2, linestyle="--")

    plt.scatter([best_epoch], [best_val_acc], color="#004D40", s=90, zorder=5,
                label=f"Peak Validation: {best_val_acc:.2f}% (Epoch {best_epoch})")

    plt.title("EfficientNetB0 - Training vs. Validation Accuracy", fontsize=14, fontweight="bold", pad=12)
    plt.xlabel("Training Epochs", fontsize=12, labelpad=8)
    plt.ylabel("Accuracy (%)", fontsize=12, labelpad=8)
    plt.ylim(20, 102)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="lower right", frameon=True, fontsize=11)
    plt.tight_layout()

    acc_path = REPORTS_DIR / "accuracy_curve.png"
    plt.savefig(acc_path, dpi=300)
    print(f"[OK] Saved Accuracy Curve    -> {acc_path}")
    plt.close()

    # ================================================================
    # 2. LOSS CURVE
    # ================================================================
    plt.figure(figsize=(9, 5.5), dpi=300)
    plt.plot(epochs, train_loss, label="Training Loss", color="#1E88E5", linewidth=2.2)
    plt.plot(epochs, val_loss, label="Validation Loss", color="#D81B60", linewidth=2.2, linestyle="--")

    plt.title("EfficientNetB0 - Categorical Cross-Entropy Loss", fontsize=14, fontweight="bold", pad=12)
    plt.xlabel("Training Epochs", fontsize=12, labelpad=8)
    plt.ylabel("Loss Value", fontsize=12, labelpad=8)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="upper right", frameon=True, fontsize=11)
    plt.tight_layout()

    loss_path = REPORTS_DIR / "loss_curve.png"
    plt.savefig(loss_path, dpi=300)
    print(f"[OK] Saved Loss Curve        -> {loss_path}")
    plt.close()

    # ================================================================
    # 3. COMBINED DASHBOARD (2-IN-1 FOR PPT / REPORT)
    # ================================================================
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), dpi=300)

    # Subplot 1: Accuracy
    ax1.plot(epochs, train_acc, label="Training Accuracy", color="#1E88E5", linewidth=2.2)
    ax1.plot(epochs, val_acc, label="Validation Accuracy", color="#D81B60", linewidth=2.2, linestyle="--")
    ax1.scatter([best_epoch], [best_val_acc], color="#004D40", s=80, zorder=5,
                label=f"Peak Val: {best_val_acc:.2f}% (Epoch {best_epoch})")
    ax1.set_title("Classification Accuracy", fontsize=13, fontweight="bold")
    ax1.set_xlabel("Epoch", fontsize=11)
    ax1.set_ylabel("Accuracy (%)", fontsize=11)
    ax1.set_ylim(20, 102)
    ax1.grid(True, linestyle=":", alpha=0.6)
    ax1.legend(loc="lower right", fontsize=10)

    # Subplot 2: Loss
    ax2.plot(epochs, train_loss, label="Training Loss", color="#1E88E5", linewidth=2.2)
    ax2.plot(epochs, val_loss, label="Validation Loss", color="#D81B60", linewidth=2.2, linestyle="--")
    ax2.set_title("Categorical Cross-Entropy Loss", fontsize=13, fontweight="bold")
    ax2.set_xlabel("Epoch", fontsize=11)
    ax2.set_ylabel("Loss", fontsize=11)
    ax2.grid(True, linestyle=":", alpha=0.6)
    ax2.legend(loc="upper right", fontsize=10)

    fig.suptitle("Plant Disease Detection (62 Classes) - Performance Dashboard", fontsize=15, fontweight="bold")
    plt.tight_layout()

    dashboard_path = REPORTS_DIR / "performance_dashboard.png"
    plt.savefig(dashboard_path, dpi=300)
    print(f"[OK] Saved Combined Dashboard -> {dashboard_path}")

    print("=" * 70)
    print(f"Summary:")
    print(f"  * Total Epochs       : {len(epochs)}")
    print(f"  * Peak Validation Acc: {best_val_acc:.2f}% (Epoch {best_epoch})")
    print(f"  * Final Validation Acc: {final_val_acc:.2f}%")
    print("=" * 70)

    # Re-plot dashboard for interactive display window
    plt.show()


if __name__ == "__main__":
    generate_performance_graphs()

