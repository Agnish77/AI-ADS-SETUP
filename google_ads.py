import google.ads.google_ads.client

def create_google_ad(data):
    client = google.ads.google_ads.client.GoogleAdsClient.load_from_storage()

    campaign_service = client.get_service("CampaignService")
    campaign_operation = client.get_type("CampaignOperation")

    campaign = campaign_operation.create
    campaign.name = data.get("campaign_name", "AI Generated Campaign")
    campaign.status = client.enums.CampaignStatusEnum.ENABLED
    campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.SEARCH

    campaign_service.mutate_campaigns(customer_id="YOUR_CUSTOMER_ID", operations=[campaign_operation])
    
    return {"campaign_name": campaign.name, "status": "Created"}
