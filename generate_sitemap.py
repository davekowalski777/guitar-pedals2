import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guitar_pedals.settings')
django.setup()

from pedals.models import Pedal, Manufacturer

def generate_sitemap():
    sitemap_content = """<?xml version='1.0' encoding='utf-8'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <!-- Main Pages -->
    <url><loc>https://guitarpedaldb.com/</loc></url>
    <url><loc>https://guitarpedaldb.com/pedals/</loc></url>
    <url><loc>https://guitarpedaldb.com/manufacturers/</loc></url>
    <url><loc>https://guitarpedaldb.com/about/</loc></url>
    <url><loc>https://guitarpedaldb.com/privacy-policy/</loc></url>

    <!-- Guide Pages -->
    <url><loc>https://guitarpedaldb.com/guides/what-are-guitar-pedals/</loc></url>
    <url><loc>https://guitarpedaldb.com/guides/how-to-choose-guitar-pedals/</loc></url>
    <url><loc>https://guitarpedaldb.com/guides/guitar-pedal-chain/</loc></url>
    <url><loc>https://guitarpedaldb.com/guides/pedals-for-beginners/</loc></url>
    <url><loc>https://guitarpedaldb.com/guides/are-pedals-necessary/</loc></url>

    <!-- Manufacturer Pages -->"""

    # Add manufacturer pages
    for manufacturer in Manufacturer.objects.all():
        sitemap_content += f"""
    <url><loc>https://guitarpedaldb.com/manufacturer/{manufacturer.name.lower().replace(' ', '-')}/</loc></url>"""

    sitemap_content += "\n\n    <!-- Pedal Pages -->"

    # Add all pedal pages
    for pedal in Pedal.objects.all().select_related('manufacturer'):
        # Remove "-review" from slug if it's already there
        clean_slug = pedal.slug[:-7] if pedal.slug.endswith('-review') else pedal.slug
        sitemap_content += f"""
    <url><loc>https://guitarpedaldb.com/pedal/{clean_slug}-review/</loc></url>"""

    sitemap_content += """
</urlset>"""

    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

if __name__ == '__main__':
    generate_sitemap()
