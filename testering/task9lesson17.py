import seaborn as sns
import matplotlib.pyplot as plt

# 1. Załadowanie danych
penguins = sns.load_dataset('penguins')

# Ustawienie stylu wizualizacji
sns.set_theme(style="whitegrid")

# 2. Tworzenie figury i osi (grid 2x2)
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Dashboard EDA: Palmer Penguins Dataset', fontsize=20, fontweight='bold')

# --- WYKRES 1: Rozkład masy ciała (Histogram z KDE) ---
sns.histplot(data=penguins, x='body_mass_g', kde=True, color='teal', ax=axes[0, 0])
axes[0, 0].set_title('Rozkład masy ciała pingwinów', fontsize=14)
axes[0, 0].set_xlabel('Masa ciała (g)')
axes[0, 0].set_ylabel('Częstotliwość')

# --- WYKRES 2: Bill Length vs Bill Depth (Scatter plot) ---
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='species', palette='viridis', ax=axes[0, 1])
axes[0, 1].set_title('Długość vs Głębokość dzioba', fontsize=14)
axes[0, 1].set_xlabel('Długość dzioba (mm)')
axes[0, 1].set_ylabel('Głębokość dzioba (mm)')

# --- WYKRES 3: Flipper Length według gatunku (Box plot) ---
sns.boxplot(data=penguins, x='species', y='flipper_length_mm', palette='Set2', ax=axes[1, 0])
axes[1, 0].set_title('Długość płetwy według gatunku', fontsize=14)
axes[1, 0].set_xlabel('Gatunek')
axes[1, 0].set_ylabel('Długość płetwy (mm)')

# --- WYKRES 4: Liczebność według gatunku i płci (Bar plot) ---
# Używamy countplot do zliczenia wystąpień
sns.countplot(data=penguins, x='species', hue='sex', palette='pastel', ax=axes[1, 1])
axes[1, 1].set_title('Liczebność według gatunku i płci', fontsize=14)
axes[1, 1].set_xlabel('Gatunek')
axes[1, 1].set_ylabel('Liczba osobników')

# Optymalizacja układu
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Wyświetlenie dashboardu
plt.show()