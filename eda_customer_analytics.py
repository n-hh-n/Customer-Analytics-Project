import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Load the cleaned customer data
df = pd.read_csv('cleaned_customer_data_for_analysis.csv')

# Set plot style
sns.set(style="whitegrid")

# Save all EDA visualizations to a single PDF
with PdfPages('customer_full_eda_report.pdf') as pdf:

    # ✅ 1. Customer Demographics - Age Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], bins=10, kde=True, color='skyblue')
    plt.title('Age Distribution of Customers')
    plt.xlabel('Age')
    plt.ylabel('Number of Customers')
    pdf.savefig()
    plt.close()

    # ✅ 2. Gender Distribution (Pie Chart)
    plt.figure(figsize=(6, 6))
    df['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightgreen'])
    plt.title('Gender Distribution')
    pdf.savefig()
    plt.close()

    # ✅ 3. Customer Location (Top 10 Locations)
    plt.figure(figsize=(12, 6))
    df['Location'].value_counts().head(10).plot(kind='bar', color='purple')
    plt.title('Top 10 Customer Locations')
    plt.xlabel('Location')
    plt.ylabel('Number of Customers')
    pdf.savefig()
    plt.close()

    # ✅ 4. Purchasing Behavior - Total Purchase Amount Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Total Purchase Amount'], bins=20, color='orange')
    plt.title('Total Purchase Amount Distribution')
    plt.xlabel('Total Purchase Amount (USD)')
    plt.ylabel('Number of Customers')
    pdf.savefig()
    plt.close()

    # ✅ 5. Top Product Categories
    plt.figure(figsize=(12, 6))
    df['Category'].value_counts().head(10).plot(kind='bar', color='coral')
    plt.title('Top 10 Product Categories')
    plt.xlabel('Product Category')
    plt.ylabel('Number of Purchases')
    pdf.savefig()
    plt.close()

    # ✅ 6. Preferred Payment Methods
    plt.figure(figsize=(8, 6))
    df['Payment Method'].value_counts().plot(kind='bar', color='teal')
    plt.title('Preferred Payment Methods')
    plt.xlabel('Payment Method')
    plt.ylabel('Number of Customers')
    pdf.savefig()
    plt.close()

    # ✅ 7. Customer Segmentation - Purchase Frequency Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Purchase Frequency'], bins=10, color='lightcoral')
    plt.title('Purchase Frequency Distribution')
    plt.xlabel('Number of Purchases')
    plt.ylabel('Number of Customers')
    pdf.savefig()
    plt.close()

    # ✅ 8. Customer Lifetime Value (Monetary)
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Customer Lifetime Value'], bins=20, color='gold')
    plt.title('Customer Lifetime Value Distribution')
    plt.xlabel('Monetary Value (USD)')
    plt.ylabel('Number of Customers')
    pdf.savefig()
    plt.close()

    # ✅ 9. Recency of Purchases (Days Since Last Purchase)
    if 'Recency' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df['Recency'], bins=20, color='dodgerblue')
        plt.title('Recency of Purchases')
        plt.xlabel('Days Since Last Purchase')
        plt.ylabel('Number of Customers')
        pdf.savefig()
        plt.close()

print("✅ Full EDA Report saved as 'customer_full_eda_report.pdf'")

